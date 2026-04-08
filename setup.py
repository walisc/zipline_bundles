import os
from setuptools import setup, find_packages

setup(
    name="zipline_bundles",
    version="0.1",
    packages=[".", "zipline_bundles"],
    entry_points = {
        'console_scripts': ['zipline_bundles-install=install:main'],
    },
    install_requires=[
        'yahoofinancials',
        'iexfinance',
        'python-binance',
        'logbook',
   ]
)
