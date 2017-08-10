#! /usr/bin/env python3

import unittest
from hsiri import timeStringToSec

class TimerTestCase(unittest.TestCase):
    """Tests for the timer"""

    def test_timeStringToSec(self):
        self.assertEqual(timeStringToSec("3h23m5s"), 3 * 3600 + 23 * 60 + 5)
        self.assertEqual(timeStringToSec("3h23m"), 3 * 3600 + 23 * 60)
        self.assertEqual(timeStringToSec("3h5s"), 3 * 3600 + 5)
        self.assertEqual(timeStringToSec("23m5s"), 23 * 60 + 5)
        self.assertEqual(timeStringToSec("3h"), 3 * 3600)
        self.assertEqual(timeStringToSec("23m"), 23 * 60)
        self.assertEqual(timeStringToSec("5s"), 5)
        self.assertEqual(timeStringToSec("5"), 5)

if __name__ == '__main__':
        unittest.main()
