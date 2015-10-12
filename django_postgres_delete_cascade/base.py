##############################################################################
#
# Copyright (c) 2015, 2degrees Limited.
# Copyright (c) 2009, Ari Flinkman and DjangoSnippets.org user "mjt".
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

from django.db.backends.postgresql_psycopg2 import base as psycopg2_adapter_mod

from django_postgres_delete_cascade.creation import DatabaseCreation


class DatabaseWrapper(psycopg2_adapter_mod.DatabaseWrapper):

    def __init__(self, *args, **kwargs):
        super(DatabaseWrapper, self).__init__(*args, **kwargs)
        self.creation = DatabaseCreation(self)


DatabaseError = psycopg2_adapter_mod.DatabaseError

IntegrityError = psycopg2_adapter_mod.IntegrityError
