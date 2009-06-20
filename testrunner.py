"""
Test runner to run all test suites.
"""

import unittest

import test.finsignia.gae.loader as loader_tests
import test.finsignia.gae.controllers as controllers_tests
import test.finsignia.gae.router as router_tests

__TEST_MODULES__ = [loader_tests, controllers_tests, router_tests]

def run_suite():
  suites = []
  for module in __TEST_MODULES__:
    test_cases = module.test_cases()
    for test_case in test_cases:
      suites.append(load_tests(test_case))
  alltests = unittest.TestSuite(suites)
  unittest.TextTestRunner(verbosity=2).run(alltests)

def load_tests(test_case):
  return unittest.TestLoader().loadTestsFromTestCase(test_case)

if '__main__' == __name__:
  run_suite()

