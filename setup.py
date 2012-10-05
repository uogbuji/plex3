# -*- coding: utf-8 -*-
from distutils.core import setup
import sys, os
import re

here = os.path.abspath(os.path.dirname(__file__))

v = open(os.path.join(here, 'lib', '__init__.py'))
version = re.compile(r".*__version__ = '(.*?)'", re.S).match(v.read()).group(1)
v.close()

try:
    README = open(os.path.join(here, 'README.txt')).read()
    CHANGES = open(os.path.join(here, 'CHANGES.txt')).read()
except IOError:
    README = CHANGES = ''

setup(name='plex3',
      version=version,
      description="Plex is a library building lexical analysers.  This is an experimental port to Python 3",
      long_description=README + '\n\n' +  CHANGES,
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='',
      author='Greg Ewing',
      author_email='greg@cosc.canterbury.ac.nz',
      maintainer= 'Stephane Klein and Uche Ogbuji',
      maintainer_email= 'stephane@harobed.org, uche@ogbuji.net',
      url='http://www.cosc.canterbury.ac.nz/greg.ewing/python/Plex/',

      license='LGPL',
      package_dir={'plex3': 'lib'},
      packages = ['plex3',],
      #include_package_data=True,
      #install_requires=[
          # -*- Extra requirements: -*-
      #    'nose',
      #    'sphinx'
      #],
      )
