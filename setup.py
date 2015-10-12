##############################################################################
#
# Copyright (c) 2015, 2degrees Limited.
# All Rights Reserved.
#
# This file is part of django-postgres-delete-cascade
# <https://github.com/2degrees/django-postgres-delete-cascade>, which is subject
# to the provisions of the BSD at
# <http://dev.2degreesnetwork.com/p/2degrees-license.html>. A copy of the
# license should accompany this distribution. THIS SOFTWARE IS PROVIDED "AS IS"
# AND ANY AND ALL EXPRESS OR IMPLIED WARRANTIES ARE DISCLAIMED, INCLUDING, BUT
# NOT LIMITED TO, THE IMPLIED WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST
# INFRINGEMENT, AND FITNESS FOR A PARTICULAR PURPOSE.
#
##############################################################################

import os

from setuptools import find_packages
from setuptools import setup


_PARENT_DIRECTORY_PATH = os.path.abspath(os.path.dirname(__file__))


def _read_file(file_name):
    file_ = open(os.path.join(_PARENT_DIRECTORY_PATH, file_name))
    file_body = file_.read().strip()
    return file_body


setup(
    name='django-postgres-delete-cascade',
    version=_read_file('VERSION.txt'),
    description='PostgreSQL engine for Django that supports "ON DELETE CASCADE" at the database level',
    long_description=_read_file('README.rst'),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Topic :: Database',
        ],
    keywords='django postgres cascade cascading delete foreign key keys',
    author='2degrees Limited',
    author_email='2degrees-floss@googlegroups.com',
    url='https://github.com/2degrees/django-postgres-delete-cascade',
    license='BSD (http://dev.2degreesnetwork.com/p/2degrees-license.html)',
    packages=find_packages(),
    install_requires=[
        'Django >= 1.6',
        'psycopg2 >= 2.5',
        ],
    )
