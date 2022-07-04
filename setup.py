from setuptools import setup, find_packages, Extension
from distutils.command.sdist import sdist as _sdist

from Cython.Build import cythonize



extensions = [
    Extension(
        'PyPrinter',
        [ "PyPrinter.pyx" ],
        language='c++',
        extra_compile_args=[
            "-std=c++11", "-Ofast", "-pthread"
        ],
    ),
]

    
extensions = cythonize(extensions)


setup(
    name = 'PyPrinter',
    ext_modules = extensions,
)