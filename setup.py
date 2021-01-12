#!/usr/bin/env python3

from setuptools import setup

setup(
    name='reclada.parser.csv',
    description='CSV parsing step for Reclada Parser',
    version='0.1',
    packages=['reclada.parser', 'reclada.parser.csv'],
    install_requires=[
    ],
    entry_points={
        'console_scripts': ['reclada-csv-parser=reclada.parser.csv.main:main'],
    },
    python_requires='>=3.6',
)
