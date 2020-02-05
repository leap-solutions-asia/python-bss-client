from setuptools import setup, find_packages

__version__ = '0.2.3'

setup(
    name="bss-client",
    url="https://github.com/leap-solutions-asia/python-bss-client",
    version=__version__,
    packages=find_packages(),
    description="CPBM BSS API client.",
    author="tsuru",
    author_email="atsushi.m@leapsolutions.co.th",
    include_package_data=True,
    install_requires=[
        "requests==2.22.0"
    ],
    extras_require={
        'tests': [
            "pytest==5.3.2",
            "flake8==3.7.9",
            "mock==3.0.5",
            "freezegun==0.3.13",
        ],
    },
    entry_points={
        'console_scripts': [
            'bss = bss_client:main',
        ],
    },
)
