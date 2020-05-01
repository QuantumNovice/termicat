from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

ext_modules = [
    Extension("termicat",  ["termicat.py"]),
    #Extension("mymodule2",  ["mymodule2.py"]),#   ... all your modules that need be compiled ...]setup(
 ]
 
for e in ext_modules:
    e.cython_directives = {'language_level': "3"} #all are Python-3

setup(
    name = 'termicat',
    cmdclass = {'build_ext': build_ext},
    ext_modules = ext_modules
)
