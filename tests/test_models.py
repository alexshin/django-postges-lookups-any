#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_django-postges-lookups-any
------------

Tests for `django-postges-lookups-any` models module.
"""

from django.test import TestCase
from django.db.models import Subquery

from django_postges_lookups_any.test_utils.test_app.models import ModelA, ModelB

_NUM_ITEMS = 1000

class TestDjango_postges_lookups_any(TestCase):
    _num_items = _NUM_ITEMS

    @classmethod
    def setUpTestData(cls):
        cls.model_a_items = [ModelA.objects.create(name=f'Inst A {i}', external_id=i) for i in range(cls._num_items)]
        cls.model_b_items = [ModelB.objects.create(name=f'Inst B {i}', external_id=i) for i in range(cls._num_items)]

    def test__rows_exist(self):
        self.assertEqual(len(self.model_a_items), ModelA.objects.count())
        self.assertEqual(len(self.model_b_items), ModelB.objects.count())
        self.assertEqual(1000, ModelA.objects.order_by('-id')[0].pk)
        self.assertEqual(1000, ModelB.objects.order_by('-id')[0].pk)

    def test__single_static_condition(self):
        self.assertEqual(5, ModelA.objects.filter(external_id__any_arr=[1, 2, 3, 4, 5]).count())
        self.assertEqual(3, ModelA.objects.filter(external_id__any_arr=['1', '2', '3']).count())

    def test__single_subquery(self):
        model_a__instances = ModelA.objects.filter(external_id__lt=10).only('external_id')
        subquery = Subquery(model_a__instances.values('external_id'))
        model_b__instances = ModelB.objects.filter(external_id__any_arr=subquery)

        self.assertEqual(10, model_b__instances.count())

    def test__single_static_exclusion(self):
        self.assertEqual(self._num_items - 5, ModelA.objects.exclude(external_id__any_arr=[1, 2, 3, 4, 5]).count())

    def test__single_subquery_exclusion(self):
        model_a__instances = ModelA.objects.exclude(external_id__lt=10).only('external_id')
        subquery = Subquery(model_a__instances.values('external_id'))
        model_b__instances = ModelB.objects.filter(external_id__any_arr=subquery)

        self.assertEqual(self._num_items - 10, model_b__instances.count())
