from distutils.core import setup
from Cython.Build import cythonize

setup(ext_modules=cythonize("cython_demo.pyx"), )

# To compile: python setup.py build_ext --inplace