"""
Extensions to the Google AppEngine webapp framework.
"""

import os

from google.appengine.ext import webapp
import google.appengine.ext.webapp.template as templating

class ApplicationController(webapp.RequestHandler):
  def default_template_path(self):
    return os.path.join(os.path.dirname(__file__), 'templates')
    
  def template_path(self):
    return self.default_template_path()
    
  def render(self, template='', data={}):
    path = os.path.join(self.template_path(), template)
    return templating.render(path, data)

class ResourceController(ApplicationController):
  def initialize(self, request, response):
    super(ResourceController, self).initialize(request, response)
  
  def get(self, *args):
    self._index(*args)
  
  def post(self, *args):
    self._create(*args)
  
  def delete(self, *args):
    self._destroy(*args)
  
  def _index(self, *args):
    cls = self.modelClass()
    objects = cls.all()
    self.render(self.templateMappings['index'], {'objects': objects}) 
  
  def _create(self, *args):
    cls = self.modelClass()
    obj = cls()
    for field in self.objectFields():
      setattr(obj, field, self.request.get(field))
    obj.put()
  
  def _destroy(self, *args):
    cls = self.modelClass()
    obj = cls.get_by_id(self.request.get('id'))
    obj.delete()
  
  def modelClass(self):
    """
    Must be overridden by subclasses
    """
    raise NotImplementedError
  
  def templateMappings(self):
    """
    Must be overridden by subclasses
    """
    raise NotImplementedError
  
  def objectFields(self):
    """
    Must be overridden by subclasses
    """
    raise NotImplementedError
