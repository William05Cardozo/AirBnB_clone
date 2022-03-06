#!/usr/bin/python3
"""Imports modules testers"""
from datetime import datetime
import unittest
import pep8
from models.place import Place


class TestPlace(unittest.TestCase):
    """Testing"""

    @classmethod
    def setUpClass(cls):
        """instance"""
        cls.placemodel = Place()
        cls.placemodel.number_rooms = 1
        cls.placemodel.city_id = 'cali'
        cls.placemodel.user_id = '1516dgb1d'
        cls.placemodel.name = 'william'
        cls.placemodel.description = 'sensey'
        cls.placemodel.number_bathrooms = 2
        cls.placemodel.max_guest = 5
        cls.placemodel.price_by_night = 3
        cls.placemodel.latitude = 5.8
        cls.placemodel.longitude = 6.7
        cls.placemodel.amenity_ids = ["cali", "medellin", "bogota"]
        cls.placedict = cls.placemodel.to_dict()
        cls.diccinary = Place(**cls.placedict)

    def test_pep8(self):
        """Test of style"""
        st = pep8.StyleGuide(quiet=True)
        stx = st.check_files(['models/place.py'])
        self.assertEqual(stx.total_errors, 0, "check pep8")

    def test_docstring(self):
        """Test of docstring"""
        self.assertTrue(len(self.placemodel.__doc__) > 0)

    def test_atribute(self):
        """validation number"""
        self.assertIsInstance(self.placemodel.number_bathrooms, int)
        self.assertIsInstance(self.placemodel.city_id, str)
        self.assertIsInstance(self.placemodel.user_id, str)
        self.assertIsInstance(self.placemodel.name, str)
        self.assertIsInstance(self.placemodel.description, str)
        self.assertIsInstance(self.placemodel.number_rooms, int)
        self.assertIsInstance(self.placemodel.max_guest, int)
        self.assertIsInstance(self.placemodel.price_by_night, int)
        self.assertIsInstance(self.placemodel.longitude, float)
        self.assertIsInstance(self.placemodel.latitude, float)
        self.assertIsInstance(self.placemodel.amenity_ids, list)
        self.assertIsInstance(self.placemodel.created_at, datetime)
        self.assertIsInstance(self.placedict, dict)
        self.assertIsInstance(self.placemodel.id, str)
        self.assertIsInstance(self.placemodel.__str__(), str)


if __name__ == '__main__':
    unittest.main()
