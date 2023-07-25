"""The setup script."""

import os
from setuptools import setup, find_packages
import codecs

# Base directory of package
here = os.path.abspath(os.path.dirname(__file__))


def read(*parts):
    with codecs.open(os.path.join(here, *parts), 'r') as fp:
        return fp.read()
def read_requires():
    with open(os.path.join(here, "ant_gen/requirements.txt"),
              "r") as reqfile:
        return reqfile.read().splitlines()

with open("README.md", "r") as fh:
    readme = fh.read()


setup(
    name='ant_gen',
    version='0.3.0',
    description="SOC Generator",
    long_description= readme + '\n\n',
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "License :: MIT",
        "Development Status :: Beta"
    ],
    keywords = "ant_gen",
    url = 'https://github.com/JoyenBenitto/Antenna_generator',
    author = "Joyen Benitto",
    author_email = 'joyen.benitto12@gmail.com',
    license = "MIT License",
    packages = find_packages(),
    install_requires = ["requests"],
    python_requires = ">=3.8",
    entry_points={
        'console_scripts': ['ant_gen=ant_gen.main:cli'],
    },
    include_package_data=True,
    tests_require=[],
    zip_safe=False
)
