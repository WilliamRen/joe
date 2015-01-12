#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='joe',
    version='0.0.1',
    description='joe generates .gitignore files from the command line for you.',
    author='Karan Goel',
    author_email='karan@goel.io',
    license='MIT',
    keywords="gitignore command line cli",
    url='http://github.com/karan/joe',
    packages=find_packages(),
    package_data={
        'joe': ['data/*.gitignore']
    },
    install_requires=[
        "docopt==0.6.1",
    ],
    entry_points={
        'console_scripts': [
            'joe=joe.joe:main'
        ],
    }
)
