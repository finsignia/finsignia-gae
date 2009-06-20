"""
Tests for finsignia.gae.router module
"""
from finsignia.gae import loader

import unittest

class RouteMapperTest(unittest.TestCase):
  def setUp(self):
    loader.load()
    from finsignia.gae import router
    from finsignia.gae import controllers
    self._routeMapper = router.RouteMapper()
    self._testController = controllers.ApplicationController()
    pass
  
  def tearDown(self):
    self._routeMapper.clear()
    
  def testConnect(self):
    oldRoutes = self._routeMapper.routes()
    self._routeMapper.connect('/path', self._testController)
    newRoutes = self._routeMapper.routes()
    self.assertNotEqual(oldRoutes, newRoutes)
    self.assertEqual(len(oldRoutes) + 1, len(newRoutes))

def test_cases():
  return [RouteMapperTest]

if '__main__' == __name__:
  unittest.main()
