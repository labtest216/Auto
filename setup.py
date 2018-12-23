#!/usr/bin/python3
from setuptools import setup

setup(
    name='Auto',
    packages=['Listeners', 'Sensors', 'Utils', 'HwModule'],
    include_package_data=True,
    install_requires=[
        'flask',
    ],
)