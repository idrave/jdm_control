#!/usr/bin/env python

from setuptools import setup, find_packages

required = [
    'jax>=0.3.4',
    'jaxlib>=0.3.2',
]

setup(
    name='jdm_control',
    version='0.0.1',
    packages=find_packages(),
    python_requires='>=3.8',
    install_requires=required,
    )
