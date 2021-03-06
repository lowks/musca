#!/usr/bin/env python
# -*- coding: utf-8 -*-

from distutils.core import setup

setup(name='musca',
      version='0.0.2',
      description='Another way to control musca.',
      long_description=open('README.md').read(),
      author='solos',
      author_email='solos@solos.so',
      py_modules=['musca', 'keycodes'],
      scripts=['musca.py', 'keycodes.py', 'musca_test.py'],
      classifiers=[
          'Intended Audience :: End Users/Desktop',
          'License :: OSI Approved :: MIT License',
          'Environment :: Console',
          'Natural Language :: English',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Topic :: Utilities',
      ],
      license='MIT',
      install_requires=['virtkey'],
      url='https://github.com/solos/musca')
