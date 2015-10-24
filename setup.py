#!/usr/bin/env python

import sys
import os
from setuptools import setup, find_packages

_top_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_top_dir, "lib"))
try:
    import markdown_tag
finally:
    del sys.path[0]
README = open(os.path.join(_top_dir, 'README.md')).read()

setup(name='django-markdown-tag',
    version=markdown_tag.__version__,
    description="a Django app that provides template tags for using Markdown (using the python-markdown processor)",
    long_description=README,
    classifiers=[c.strip() for c in """
        Development Status :: 5 - Production/Stable
        Environment :: Web Environment
        Framework :: Django
        Intended Audience :: Developers
        License :: OSI Approved :: MIT License
        Operating System :: OS Independent
        Programming Language :: Python :: 2
        Topic :: Internet :: WWW/HTTP
        """.split('\n') if c.strip()],
    keywords='django markdown text markup html',
    author='Trent Mick, Steffen Görtz',
    author_email='trentm@gmail.com, steffen@steffen-goertz.de',
    maintainer='Steffen Görtz',
    maintainer_email='steffen@steffen-goertz.de',
    url='http://github.com/douzepouze/django-markdown-tag',
    license='MIT',
    install_requires = ['markdown'],
    packages=["markdown_tag"],
    package_dir={"": "lib"},
    include_package_data=True,
    zip_safe=False,
)

