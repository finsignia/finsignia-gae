"""
Router to help DRY up path/controller mappings more intuitively than the WSGI API
"""

from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

import copy

class RouteMapper:
  """
  Convenience class that makes it cleaner and easier to create route mappings from 
  a path to a controller class.
  """
  def __init__(self):
    self._mappings = []
    
  def connect(self, path, controller):
    self._mappings.append((path, controller))
    
  def routes(self):
    return copy.copy(self._mappings)
  
  def clear(self):
    self._mappings = []
  
  def run(self):
    run_wsgi_app(webapp.WSGIApplication(self._mappings, debug=True))

