"""
Setup script for ML Pipeline Project
=====================================

This file allows the package to be installed using pip.
For most purposes, use pyproject.toml with `pip install -e .`
"""

from setuptools import setup, find_packages

setup(
    packages=find_packages(where="src"),
    package_dir={"": "src"},
)
