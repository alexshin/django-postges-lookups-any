=====
Usage
=====

To use django-postgres-lookups-any in a project, add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'django_postges_lookups_any.apps.DjangoPostgesLookupsAnyConfig',
        ...
    )

Add django-postgres-lookups-any's URL patterns:

.. code-block:: python

    from django_postges_lookups_any import urls as django_postges_lookups_any_urls


    urlpatterns = [
        ...
        url(r'^', include(django_postges_lookups_any_urls)),
        ...
    ]
