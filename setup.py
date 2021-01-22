# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
#
# Author: Nuno Fachada

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name = "finefibo",
    version = "0.1.0",
    author = "Nuno Fachada",
    author_email = "nuno.fachada@ulusofona.pt",
    description = "Fine Fibonacci numbers!",
    long_description = long_description,
    long_description_content_type='text/markdown',
    url = "https://github.com/fakenmc/finefibo",
    # Automate below with
    # setuptools.find_packages()
    packages = ['finefibo'],
    # We don't actually need numpy
    # install_requires = ['numpy'],
    python_requires = '>=3.6',
)
