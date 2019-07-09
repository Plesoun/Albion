from unittest import TestCase
from unittest.mock import patch
from src.creator import Creator


class TestCreator(TestCase):
    def setUp(self):
        self.creator = Creator(
            subset_name="tracked_items",
            item_of_interest="T1_CARROT",
            db_csv="db",
        )

    def test_create_frame(self):
        self.assertEqual(
            str(type(self.creator.create_frame())),
            "<class 'pandas.core.frame.DataFrame'>",
        )
        self.assertEqual(len(self.creator.create_frame().columns), 11)
