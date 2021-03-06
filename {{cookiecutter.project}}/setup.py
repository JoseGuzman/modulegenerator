"""
setup.py

Author: {{cookiecutter.author}}, {{cookiecutter.mail}} 
Created: {% now 'local', '%d/%m/%Y' %}

Installation file required for the {{cookiecutter.module}}  module
"""
import os
import re
import os.path as op
from setuptools import setup 

#-------------------------------------------------------------------------
# setup
#-------------------------------------------------------------------------
def _package_tree(pkgroot):
    path = op.dirname(__file__)
    subdirs = [op.relpath(i[0], path).replace(op.sep, '.')
               for i in os.walk(op.join(path, pkgroot))
               if '__init__.py' in i[2]]
    return subdirs


# read README.md
curdir = op.dirname(op.realpath(__file__))
with open(op.join(curdir, 'README.md')) as f:
    myreadme = f.read()

# Find version number from `__init__.py` without executing it.
filename = op.join(curdir, '{{cookiecutter.module}}/__init__.py')
with open(filename, 'r') as f:
    myversion = re.search(r"__version__ = '([^']+)'", f.read()).group(1)


setup(
    name = '{{cookiecutter.module}}', # application name
    version = myversion,# application version
    license = 'LICENSE',
    description = '{{cookiecutter.module}} is a Python module',
    long_description = myreadme,
    author = '{{cookiecutter.author}}',
    author_email = '{{cookiecutter.mail}}',
    packages = ['{{cookiecutter.module}}'],
    python_requires='>=3.5',
    include_package_data = True,# include additional data
    package_data={
        # If any package contains *.txt files, include them:
        '': ['*.txt'],
        # And include any *.csv files in the 'datasets' subdirectory
        # of the '{{cookiecutter.module}}' package, also:
        '{{cookiecutter.module}}': ['datasets/*.csv'],
    },
)
