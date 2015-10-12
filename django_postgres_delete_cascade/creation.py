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

from django.db.backends.postgresql_psycopg2.base import \
    DatabaseCreation as OriginalDatabaseCreation


class DatabaseCreation(OriginalDatabaseCreation):

    def sql_for_inline_foreign_key_references(
        self,
        model,
        field,
        known_models,
        style,
        ):
        fk_references, is_pending = \
            super(DatabaseCreation, self).sql_for_inline_foreign_key_references(
                model,
                field,
                known_models,
                style,
                )
        if not is_pending:
            fk_references = _add_delete_cascade_to_fk_references(fk_references)
        return fk_references, is_pending

    def sql_for_pending_references(self, model, style, pending_references):
        fk_references = \
            super(DatabaseCreation, self).sql_for_pending_references(
                model,
                style,
                pending_references,
                )
        fk_references = _add_delete_cascade_to_fk_references(fk_references)
        return fk_references


def _add_delete_cascade_to_fk_references(fk_references):
    fk_references_with_cascade = []
    for fk_reference in fk_references:
        fk_reference_with_cascade = fk_reference.replace(
            'DEFERRABLE',
            'ON DELETE CASCADE DEFERRABLE',
            )
        fk_references_with_cascade.append(fk_reference_with_cascade)
    return fk_references_with_cascade
