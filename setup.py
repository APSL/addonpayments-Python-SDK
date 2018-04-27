# -*- encoding: utf-8 -*-

import os
import re
import codecs

try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup


def get_version(package):
    """
    Return package version as listed in `__version__` in `init.py`.
    """
    init_py = codecs.open(os.path.abspath(os.path.join(package, '__init__.py')), encoding='utf-8').read()
    return re.search("^__version__ = ['\"]([^'\"]+)['\"]", init_py, re.MULTILINE).group(1)


def get_author(package):
    """
    Return package author as listed in `__author__` in `init.py`.
    """
    init_py = codecs.open(os.path.abspath(os.path.join(package, '__init__.py')), encoding='utf-8').read()
    return re.search("^__author__ = ['\"]([^'\"]+)['\"]", init_py, re.MULTILINE).group(1)


def get_email(package):
    """
    Return package email as listed in `__email__` in `init.py`.
    """
    init_py = codecs.open(os.path.abspath(os.path.join(package, '__init__.py')), encoding='utf-8').read()
    return re.search("^__email__ = ['\"]([^'\"]+)['\"]", init_py, re.MULTILINE).group(1)


def get_long_description():
    """
    return the long description from README.rst file
    :return:
    """
    return codecs.open(os.path.join(os.path.dirname(__file__), 'README.rst'), encoding='utf-8').read()


setup(
    name='addonpayments-sdk-python',
    version=get_version('addonpayments'),
    author=get_author('addonpayments'),
    author_email=get_email('addonpayments'),
    url='https://github.com/ComerciaGP/addonpayments-Python-SDK',
    packages=find_packages(exclude=['tests*']),
    license='BSD',
    description='A SDK Addonpayments implemented with Python.',
    long_description=get_long_description(),
    install_requires=[
        'six',
        'python-decouple',
        'attrs>=16.3.0,<17.3.0',
        'xmltodict',
        'requests',
        'future',
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Operating System :: OS Independent',
        'Topic :: Software Development'
    ],
    include_package_data=True,
    zip_safe=False,
)
