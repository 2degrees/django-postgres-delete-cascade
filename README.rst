PostgreSQL engine for Django that supports "ON DELETE CASCADE" at the database level
====================================================================================

This is a temporary workaround until `Django's ticket #21961
<https://code.djangoproject.com/ticket/21961>`_ is fixed. It has been tested
with Python 2.7, Django 1.6 and Psycopg2 2.6, but should work with other
combinations.

To use it, you just have to:

#. Install this distribution as a dependency. For example,

    .. code-block:: bash

        pip install django-postgres-delete-cascade

#. Replace the ``django.db.backends.postgresql_psycopg2`` engine with
   ``django_postgres_delete_cascade``. For example:

    .. code-block:: python

        DATABASES = {
            'default': {
                'ENGINE': 'django_postgres_delete_cascade',
                'NAME': 'mydatabase',
                'USER': 'mydatabaseuser',
                'PASSWORD': 'mypassword',
                'HOST': '127.0.0.1',
                'PORT': '5432',
                }
            }


Change log
----------

Version 1.0 Release Candidate 3 (2015-10-12)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Fixed packaging issue.


Version 1.0 Release Candidate 2 (2015-10-12)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Initial release, in spite of the version (due to some problems with PYPI).
