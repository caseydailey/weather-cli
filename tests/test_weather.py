import sys; sys.path.append('../src/')
import unittest
# from unittest.mock import Mock
# from contextlib import contextmanager
# from StringIO import StringIO
import controller
import api


class TestWeather(unittest.TestCase):

    # TODO test I/O
    # TODO test api
    # TODO test k_to_f
    # TODO test raise right errors with bad input
    # TODO test attributes are accessible and accurate (stub a report object)
    
    

    def test_is_cold_returns_true_when_temp_is_under_60(self):
        self.assertTrue(api.is_cold(40))
    
    def test_is_cold_returns_false_when_temp_is_over_60(self):
        self.assertFalse(api.is_cold(70))



