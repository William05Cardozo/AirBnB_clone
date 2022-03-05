#!/usr/bin/python3
"""Imports modules testers"""

from pyexpat import model
import unittest
import pep8
import os
import models
from models.review import Review
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestReview(unittest.TestCase):
    """Testing"""

    @classmethod
    def setUpClass(cls):
        """instance"""
        cls.Reviewmodel = Review()

    def test_pep8(self):
        """Test of style"""
        st = pep8.StyleGuide(quiet=True)
        stx = st.check_files(['models/review.py'])
        self.assertEqual(stx.total_errors, 0, "check pep8")

    def test_docstring(self):
        """Test of docstring"""
        self.assertTrue(len(self.Reviewmodel.__doc__) > 0)


if __name__ == '__main__':
    unittest.main()