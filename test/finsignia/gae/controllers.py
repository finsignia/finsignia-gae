"""
Tests for the finsignia.gae.controllers module.
"""

import os
import sys

from finsignia.gae import loader

import unittest

class ApplicationControllerTest(unittest.TestCase):
  def setUp(self):
    loader.load()
    from finsignia.gae import controllers
    class TestController(controllers.ApplicationController):
      def template_path(self):
        return os.path.join(os.path.dirname(__file__), 'templates')

    self.controller = TestController()
    
  def tearDown(self):
    del self.controller
    loader.unload()
    
  def testRenderWithoutData(self):
    text = self.controller.render(template='testRenderWithoutData.txt')
    self.assertEqual("testRenderWithoutData", text.strip())
  
  def testRenderWithData(self):
    # I just watched 'The Reader' at the movie theatre this evening...thus the following name
    name = 'Hannah Schmidtz'
    text = self.controller.render(template='testRenderWithData.txt', data={'name': name})
    self.assertEqual("%s did a very bad thing and then a very stupid thing" % name, text.strip())

class ResourceControllerTest(unittest.TestCase):
  def setUp(self):
    loader.load()
    self._modelClass = object()
    self._templateMappings = {}
    self._objectFields = []
    from finsignia.gae import controllers
    class TestController(controllers.ResourceController):
      def modelClass(self): return self._modelClass
      def templateMappings(self): return self._templateMappings
      def objectFields(self): return self._objectFields
    self._testController = TestController()
  
  def tearDown(self):
    loader.unload()
    
  # TODO: create tests for ResourceController

def test_cases():
  return [ApplicationControllerTest, ResourceControllerTest]

if '__main__' == __name__:
  unittest.main()
