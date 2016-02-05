#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

import glossolalia

install_requires = [
    "polib",
]

setup(
    name="glossolalia",
    version=glossolalia.__version__,
    author="Fusionbox",
    author_email="programmers@fusionbox.com",
    url="https://github.com/fusionbox/glossolalia",
    description="Translation Utility to Create Pseudo Translations of PO Files",
    long_description=open('README.rst').read(),
    license=open("LICENSE").read(),
    package_data={"": ["LICENSE"]},
    packages=find_packages(exclude=('tests',)),
    zip_safe=False,
    install_requires=install_requires,
    include_package_data=True,
    entry_points={
        "console_scripts": [
            "glossolalia = glossolalia.__main__:main",
        ],
    },
    classifiers=[
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "Operating System :: OS Independent",
        "Topic :: Software Development",
    ],
)
