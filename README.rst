PostgreSQL/psycopg2 database adapter for Django that supports "ON DELETE CASCADE" at the database level
=======================================================================================================

This is a temporary workaround until Django's ticket #21961 is fixed.

To use it, you just have to:

#. Add this distribution as a dependency. For example,

    .. code-block:: bash

        pip install django-postgres-delete-cascade

#. Replace the ``django.db.backends.postgresql_psycopg2`` engine with
   ``django_postgres_delete_cascade``; e.g.:

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

That's it!
