#!/usr/bin/env python

from distutils.core import setup

setup(
  name='finsignia-gae',
  version='0.1',
  description='A Finsignia library that lays on top of the GAE webapp framework to provide extensions and helpers to DRY up application code.',
  author='Susan Potter',
  author_email='me@susanpotter.net',
  url='http://projects.susanpotter.net/open-source/python/finsignia-gae',
  packages=['finsignia.gae'],
  classifiers=[
    "License :: OSI Approved :: MIT License (MIT)",
    "Programming Language :: Python",
    "Development Status :: 4 - Beta",
    "Intended Audience :: Developers",
    "Topic :: Web",
  ],
  keywords='web framework internet google',
  license='MIT',
)
