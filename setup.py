# coding=utf-8
import os
import sys
from setuptools import setup

import vtex_client


REQUIREMENTS = ['requests']

setup(
    name="vtex-client",
    version=vtex_client.__version__,
    author="Shadi",
    author_email="geovanne.faria@jussi.com.br",
    description="Client to consume the VTEX API",
    license="MIT License",
    keywords="vtex_client",
    url="https://github.com/shaderas/vtexapwhp",
    packages=['vtex_client', 'tests'],
    namespace_packages=['vtex_client'],
    package_dir={'vtex_client': 'vtex_client'},
    install_requires=REQUIREMENTS,
    download_url="https://github.com/shaderas/vtexapwhp/blob/master",
    classifiers=[
        "Development Status :: 0 - Development",
        "Topic :: Utilities",
        "Environment :: Plugins",
        "License :: None.",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
    ],
)
