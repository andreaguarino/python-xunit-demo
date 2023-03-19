import unittest
import xmlrunner


class TestDemo(unittest.TestCase):

    def test_demo_add(self):
        from demo import add
        self.assertTrue(add(1, 1) == 2)

    def test_demo_mul(self):
        from demo import mul
        self.assertTrue(mul(1, 3) == 3)


if __name__ == '__main__':
    unittest.main(
        testRunner=xmlrunner.XMLTestRunner(output='test-reports'),
        # these make sure that some options that are not applicable
        # remain hidden from the help menu.
        failfast=False, buffer=False, catchbreak=False)
