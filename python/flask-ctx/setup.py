#!/usr/bin/env python

from setuptools import setup, find_packages


setup(
    name="flask-ctx",
    version="1.0.0",
    author="Dimitris Karakostas",
    author_email="dimit.karakostas@gmail.com",
    url="https://github.com/dimkarakostas/ctx",
    description="A simple integration of the CTX defense against side-channel attacks for Flask projects.",
    long_description=open("README.rst").read(),
    download_url="https://github.com/dimkarakostas/ctx",
    license="MIT",
    packages=find_packages(exclude=['flask_ctx.tests']),
    test_suite='nose.collector',
    tests_require=['nose', 'Flask>=0.10', 'ctx-defense'],
    include_package_data=True,
    keywords="flask ctx defense compression security BREACH",
    install_requires=[
        "Flask>=0.10",
        "ctx-defense",
    ],
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Flask",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Topic :: Security",
        "Topic :: Security :: Cryptography",
    ],
    zip_safe=False,
)
