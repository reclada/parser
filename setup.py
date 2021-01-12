#!/usr/bin/env python3

from setuptools import setup

setup(
    name='reclada.csv_parser',
    description='CSV parsing step for Reclada Parser',
    version='0.1',
    packages=['reclada.csv_parser'],
    install_requires=[
    ],
    entry_points={
        'console_scripts': ['reclada-csv-parser=reclada.csv_parser.main:main'],
    },
    python_requires='>=3.6',
)
