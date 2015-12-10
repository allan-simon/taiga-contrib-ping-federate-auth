#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='taiga-contrib-ping-federate-auth',
    version=":versiontools:taiga_contrib_ping_federate_auth:",
    description="The Taiga plugin for Ping Federate authentication",
    long_description="",
    keywords='taiga, ping federate, auth, plugin',
    author='Allan SIMON',
    author_email='allan.simon@supinfo.com',
    url='https://github.com/allan-simon/taiga-contrib-ping-federate-auth',
    license='AGPL',
    include_package_data=True,
    packages=find_packages(),
    install_requires=[
        'django >= 1.7',
    ],
    setup_requires=[
        'versiontools >= 1.8',
    ],
    classifiers=[
        "Programming Language :: Python",
        'Development Status :: 4 - Beta',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Affero General Public License v3',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
    ]
)
