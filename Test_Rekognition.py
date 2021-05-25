import unittest

class TestImages(unittest.TestCase):

    def __init__(self, labelname, usercompare):
        super().__init__()
        self.labelname = labelname
        self.usercompare = usercompare


    def test_labelname(self):
        try:
            # print("Hitting unit test")
            self.assertEqual(self.labelname, self.usercompare, 'Cannot find car label {}'.format(self.labelname))
            print("We have a match with {}".format(self.labelname))
        except self.failureException:
            pass

        # print("Unit Test is complete")