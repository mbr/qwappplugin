#!/usr/bin/env python
# coding=utf8

from distutils.core import setup

setup(name = 'qwappplugin',
      version = '0.1dev',
      description = 'Miscellaneous plugins for qwapp',
      author = 'Marc Brinkmann',
      url = 'https://github.com/qwappplugin',
      packages = ['qwappplugin'],
      namespace_packages = ['qwappplugin'],
      install_requires = ['qwapp'],
     )
