# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='my-cypto-wallet',
    version='0.1.0',
    description='My own crypto wallet',
    long_description=readme,
    author='Albert Palau',
    author_email='',
    url='https://github.com/albpal/my-crypto-wallet.git',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

