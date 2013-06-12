from  edition1.twitterportletfix.testing import EDITION1_TWITTERPORTLETFIX_FUNCTIONAL_TESTING
from plone.testing import layered
import robotsuite
import unittest


def test_suite():
    suite = unittest.TestSuite()
    suite.addTests([
        layered(robotsuite.RobotTestSuite("robot_test.txt"),
                layer=EDITION1_TWITTERPORTLETFIX_FUNCTIONAL_TESTING)
    ])
    return suite