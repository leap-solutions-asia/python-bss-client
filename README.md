[![Build Status](https://travis-ci.org/globocom/python-bss-client.svg?branch=master)](https://travis-ci.org/globocom/python-bss-client)

# CPBM BSS API Client

­CloudPortal™ Business Manager (CPBM) Business Support System (BSS) API Client

## Description

This is a minimal wrapper around CPBM BSS API.

It simplifies creating signed requests to the API and also implements a 
high-level abstraction for commonly used methods.

Ideally we'll implement high-level wrappers for every possible API calls,
however we're not there yet.

## Installation

```
$ pip install git+https://github.com/leap-solutions-asia/python-bss-client.git
```

## Basic Usage

With high-level API wrapper

```python
from bss_client import BSSClient

endpoint = 'http://myhost.com/portal/api'
key = 'my api key'
secret = 'my api secret'

client = BSSClient(endpoint, key, secret)
rsp_json = client.list_subscriptions()
print(rsp_json)
```

With low-level signed request wrapper

```python
from bss_client import BSSClient

client = BSSClient(endpoint, key, secret)
req = client.create_request()
req.add_param('tenantparam', 'uuid')
req.add_param('productbundleid', 'mybundleid')
...
rsp = req.request('POST', '/subscriptions')
print(rsp)
```

## Command Line

### Create config file

```bash
cat <<EOF > ~/.cloudstack.ini
[cpbm]
endpoint = YOUR_API_ENDPOINT
key=YOUR_API_KEY
secret= YOUR_SECRET_KEY
EOF
```

### Basic Usage

``` bash
$ bss [-m METHOD] PATH [[key=value] [key=value] ...]
```

Get account list
```bash
$ bss /accounts
```

Get account list with state is NEW
```bash
$ bss /accounts state=NEW
```

Create a new account
```bash
$ bss -m POST /accounts \
      accountname=test \
      accounttypeid=10 \
      currencycode=THB \
      ownerfirstname=Test \
      ownerlastname=Test \
      owneremail=test@example.com \
      ownerusername=test \
      countrycode=66 \
      state=test \
      city=bangkok \
      street1=test \
      zipcode=11111 \
      isdcode=1 \
      phonenumber=111111 \
      creditCardInformationCaptured=YES
```
