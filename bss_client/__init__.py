# flake8: noqa

#
import json
from argparse import ArgumentParser

#
from bss_client.client import BSSClient, read_config

#
def main(args=None):
    parser = ArgumentParser(description='CPBM BSS API Client.')
    parser.add_argument("-c", "--config", type=str,
                        help="BSS API configuration file.")
    parser.add_argument("-r", "--region", type=str, default="cpbm",
                        help=f"region in config file.")
    parser.add_argument("-m", "--method", type=str, default="GET",
                        choices=("GET", "POST", "PUT", "DELETE"),
                        help="method for BSS API.")
    parser.add_argument("path", type=str,
                        help="BSS API path to execute.")

    def parse_option(x):
        if '=' not in x:
            raise ValueError("{!r} is not a correctly formatted "
                             "option".format(x))
        return x.split('=', 1)

    parser.add_argument('arguments', metavar="OPTION=VALUE",
                        nargs='*', type=parse_option,
                        help='BSS API arguments')

    options = parser.parse_args(args=args)

    conf = read_config(options.region, options.config)

    client = BSSClient(**conf)
    req = client.create_request()

    for k, v in options.arguments:
        req.add_param(k.lower(), v)

    result = req.request(options.method, options.path)

    if result.status_code != 204:
        try:
            print(json.dumps(result.json(), sort_keys=True, indent=2))
        except:
            raise SystemExit(f'{result.status_code} : {result.text}')

    exit(0 if result.ok else 1)
