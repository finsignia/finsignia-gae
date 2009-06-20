"""
Contains methods, wrappers and helpers that load the GAE environment for bootstrapping or 
testing environments.  This module depends on GAEPATH environment variable being set to 
define the root directory of the version of Google AppEngine environment you are loading.

Usage:
  from finsignia.gae import loader
  loader.load()
"""

import sys
import os
import os.path

__all__ = ['load']

ENV_NAME = 'GAEPATH'

def gae_root():
  return os.environ[ENV_NAME]

def gae_lib_path(*paths):
  return os.path.join(gae_root(), 'lib', *paths)

PATHS = [
  gae_root(),
  gae_lib_path('django'),
  gae_lib_path('webob'),
  gae_lib_path('yaml', 'lib'),
]

def load():
  """
  Loads GAE paths into the Python environment.
  """
  for path in PATHS:
    if not os.path.exists(path):
      raise LoadError("Path does not exist: %s" % path)
    if path not in sys.path:
      sys.path.append(path)

def unload():
  """
  Unloads GAE paths from the Python environment.
  """
  for path in PATHS:
    if path in sys.path:
      sys.path.remove(path)

