# -*- coding: utf-8 -*-
"""Python client for the MediaAccount-Api"""
import sys
from setuptools import setup


REQUIREMENTS = []

with open('README.md') as README:
    LONG_DESCRIPTION = README.read()

setup(
    name='mediaaccount',
    version='2.0.0',
    url='https://github.com/ckrowiorsch/mediaaccount.py',
    license='MIT',
    author='Christian Krowiorsch',
    author_email='christian.krowiorsch@googlemail.com',
    description="Python client for the MediaAccount API",
    long_description=LONG_DESCRIPTION,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Topic :: Software Development :: Libraries",
    ],
    install_requires=REQUIREMENTS,
    tests_require=REQUIREMENTS+[
        "requests",
        "dataclasses-json"
    ],
    py_modules=['mediaaccount'],
    include_package_data=False,
    entry_points={
        'console_scripts': [
            'diffbot = diffbot:cli',
        ],
    },
    zip_safe=True,
)
