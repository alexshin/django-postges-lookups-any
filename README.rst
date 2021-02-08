=============================
django-postgres-lookups-any
=============================

.. image:: https://badge.fury.io/py/django-postges-lookups-any.svg
    :target: https://badge.fury.io/py/django-postges-lookups-any

Provides =ANY(ARRAY(xxx)) instead of IN (xxx)

Documentation
-------------

This library is designed for Postgres. It enables developers to cope with problem when Postgres
doesn't use indexes with long `IN ()` statements.

Usually, when you try to do a query:

.. code-block:: sql

    SELECT a.* FROM a
    WHERE a.id NOT IN (
        SELECT b.id FROM b
    )

You expect that it will be used index on a.id. Unfortunately, it doesn't work.

There is a trick to make Postgres do it by rewritten query this way:

.. code-block:: sql

    SELECT a.* FROM a
    WHERE a.id=ANY(ARRAY(SELECT b.id FROM b))

This library allows you to use this statement. Examples:

.. code-block:: python

    """
    SELECT * FROM mymodel WHERE somefield=ANY([1, 2, 3])
    """
    MyModel.objects.filter(somefield__any_arr=[1, 2, 3])

    """
    SELECT * FROM mymodel WHERE somefield=ANY(ARRAY(SELECT somefield FROM modelb))
    """
    subquery = Subquery(model_b__instances.values('somefield'))
    MyModel.objects.filter(somefield__any=subquery)

Quickstart
----------

Install django-postgres-lookups-any::

    pip install django-postges-lookups-any

Add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'django_postges_lookups_any',
        ...
    )

Running Tests
-------------

Does the code actually work?

::

    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install -r requirements_test.txt
    (myenv) $ pytest


Development commands
---------------------

::

    pip install -r requirements_dev.txt

Credits
-------

Tools used in rendering this package:

*  Cookiecutter_
*  `cookiecutter-djangopackage`_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-djangopackage`: https://github.com/pydanny/cookiecutter-djangopackage
