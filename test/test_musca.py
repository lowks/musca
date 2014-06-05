#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
import sys

current = os.path.dirname(os.path.abspath(__file__))
sys.path.append('%s/..' % current)

import musca
import unittest


class DefaultTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_version(self):
        self.assertIsNotNone(musca.__version__, '0.0.2')


def suite():
    suite = unittest.TestSuite()
    suite.addTest(DefaultTestCase('test_version'))
    return suite


if __name__ == '__main__':
    unittest.main(defaultTest='suite', verbosity=2)
