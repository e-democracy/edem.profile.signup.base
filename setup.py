# -*- coding=utf-8 -*-
from __future__ import absolute_import, unicode_literals
import os
from setuptools import setup, find_packages
from version import get_version

version = get_version()

setup(
    name='edem.profile.signup.base',
    version=version,
    description="E-Democracy customization to GroupServer's user registration "
                "system",
    long_description=open("README.txt").read() + "\n" +
    open(os.path.join("docs", "HISTORY.txt")).read(),
    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers for values
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Framework :: Zope2",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License v3 or later "
        "(GPLv3+)",
        "Natural Language :: English",
        "Operating System :: POSIX :: Linux"
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords='',
    author='Bill Bushey',
    author_email='bill.bushey@e-democracy.org',
    url='http://www.e-democracy.org/',
    license='GPL 3',
    packages=find_packages(exclude=['ez_setup']),
    namespace_packages=['edem', 'edem.profile', 'edem.profile.signup'],
    include_package_data=True,
    zip_safe=True,
    install_requires=[
        'setuptools',
        'edem.skin',
        'gs.profile.signup.base',
        'Products.CustomUserFolder',
        'Products.GSProfile',
        'zope.formlib',
        'Zope2'
        # -*- Extra requirements: -*-
    ],
    entry_points="""
    # -*- Entry points: -*-
    """,)
