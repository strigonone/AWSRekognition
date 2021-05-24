import unittest
from RekognitionURLImages import rekresp
# from RekognitionLocalImages import rekresp

class TestImages(unittest.TestCase):
    def test_image(self):

        self.assertAlmostEqual(rekresp("car"), "transport", "car")
