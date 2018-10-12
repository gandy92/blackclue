#!/usr/bin/env python
"""
   Copyright 2018 gandy92

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
"""

from os.path import abspath, dirname, join
from setuptools import setup, find_packages
from sys import path as sys_path

deps = [
    "pymp4",
    "click",
    "clickutil",
    "construct",
]

srcdir = join(dirname(abspath(__file__)), "blackclue/")
sys_path.insert(0, srcdir)

this_directory = abspath(dirname(__file__))
with open(join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(name="BlackClue",
      version="1.1.1",
      description="A tool to extract GPS and acceleration data from BlackVue MP4 recordings.",
      long_description=long_description,
      long_description_content_type="text/markdown",
      url="https://github.com/gandy92/blackclue",
      author="Andy Thaller",
      author_email="gandy92@googlemail.com",
      license="Apache 2.0",
      packages=find_packages("blackclue"),
      package_dir={"": "blackclue"},
      entry_points={
          "console_scripts": ["blackclue=blackclue:dump_cli"]
      },
      install_requires=deps,
      classifiers=["Development Status :: 5 - Production/Stable",
                   "Environment :: Console",
                   "Operating System :: POSIX",
                   "Programming Language :: Python :: 3",
                   "Topic :: Multimedia :: Sound/Audio",
                   "Topic :: Multimedia :: Video",
                   "Topic :: Utilities"])
