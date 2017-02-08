#!/usr/bin/env python3
from setuptools import setup
import sys

if sys.version_info < (3, 3):
    errstr = "telescope only supports python version 3.3+. Please Upgrade.\n"
    sys.stderr.write("#" * len(errstr) + '\n')
    sys.stderr.write(errstr)
    sys.stderr.write("#" * len(errstr) + '\n')
    sys.exit(1)

requirements = [
    'pygithub',
]

setup(
    name='telescope',
    description='tracking starred github repo\'s latest releases',
    long_description=open('README.rst').read(),
    author='Christian Geier',
    author_email='catcher+telescope@lostpackets.de',
    url='http://github.com/geier/telescope',
    license='Expat/MIT',
    packages=['telescope'],
    entry_points={
        'console_scripts': [
            'telescope = telescope:main',
        ]
    },
    install_requires=requirements,
    setup_requires=['setuptools_scm != 1.12.0'],  # not needed when using packages from PyPI
    use_scm_version={'write_to': 'telescope/version.py'},
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: End Users/Desktop",
        "Operating System :: POSIX",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3 :: Only",
    ],
)
