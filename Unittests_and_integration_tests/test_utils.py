#!/usr/bin/env python3
"""unit tests for utils"""
import unittest
from unittest import TestCase, mock
from unittest.mock import patch, Mock
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    """Unit Test for access_nested_map"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected_result):
        """check if function retruns expected result"""
        self.assertEqual(access_nested_map(nested_map, path), expected_result)

    @parameterized.expand([
        ({}, ("a",), 'a'),
        ({"a": 1}, ("a", "b"), 'b')
    ])
    def test_access_nested_map_exception(self, nested_map, path, exp_result):
        """ test access_nested_map
        check if funtion returns expected result
        """
        with self.assertRaises(KeyError) as raises:
            access_nested_map(nested_map, path)
            self.assertEqual(exp_result, raises.exception)


class TestGetJson(unittest.TestCase):
    """Unit test for get_json function"""
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url, test_payload):
        """ Test get_json method for utils.py
        check if the method returns the result as expected
        """
        mock = Mock()
        mock.json.return_value = test_payload
        with patch('requests.get') as mock_get:
            mock_get.return_value = mock
            result = get_json(test_url)
            self.assertEqual(result, test_payload)
            mock_get.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):
    """unit test for test_memoize function"""
    def test_memoize(self):
        """check if test_memoize returns expected result"""
        class TestClass:
            def __init__(self):
                """initialize class"""
                self.call_count = 0

            def a_method(self):
                """a_method"""
                self.call_count += 1
                return 42

            @memoize
            def a_property(self):
                """a_property"""
                return self.a_method()


if __name__ == '__main__':
    unittest.main()
