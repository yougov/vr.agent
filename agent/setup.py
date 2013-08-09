#!/usr/bin/python
from setuptools import setup, find_packages

setup(
    name='vr.common',
    namespace_packages=['vr'],
    version='2.15.2',
    author='Brent Tubbs',
    author_email='brent.tubbs@gmail.com',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Fabric==1.4.0',
        'isodate>=0.4.4',
        'mercurial>=2.6.1',
        'paramiko>=1.8.0,<2.0',
        'redis>=2.6.2',
        'suds==0.4',
    ],
    description=('Models and utils shared by other Velociraptor packages.'),
)
