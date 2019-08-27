#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name='scraper',
      version='1.0',
      description='Scrapy on openshift',
      author='MGMwerx',
      packages = find_packages(),
      entry_points =  {'scrapy': ['settings = scraper.settings']},
      url='http://www.python.org/sigs/distutils-sig/',
      install_requires=[
        'Scrapy',
        'service_identity',
      ],
     )
