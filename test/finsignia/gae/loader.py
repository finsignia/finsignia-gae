"""
Tests related to the finsignia.gae.loader module.
"""

import sys

from finsignia.gae import loader
import unittest
import mox

class LoaderTest(unittest.TestCase):
  def setUp(self):
    pass

  def tearDown(self):
    loader.unload()

  def testLoad(self):
    loader.unload()
    original_paths = sys.path
    original_size = len(original_paths)
    loader.load()
    loaded_paths = sys.path
    loaded_size = len(loaded_paths)
    self.assertNotEqual(original_size, loaded_size)
    self.assertTrue(loaded_size > original_size)
    self.assertEqual(loaded_size, original_size + 4)
    
  def testUnload(self):
    loader.load()
    loaded_paths = sys.path
    loaded_size = len(loaded_paths)
    loader.unload()
    unloaded_paths = sys.path
    unloaded_size = len(unloaded_paths)
    self.assertNotEqual(loaded_size, unloaded_paths)
    self.assertTrue(loaded_size > unloaded_size)
    self.assertEqual(loaded_size, unloaded_size + 4)

def test_cases():
  return [LoaderTest]
    
if '__main__' == __name__:
  unittest.main()

