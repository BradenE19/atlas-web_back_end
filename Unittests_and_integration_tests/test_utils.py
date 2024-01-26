#!/usr/bin/env python3
"""unit tests for utils"""
import unittest
from utils import access_nested_map

class TestAccessNestedMap(unittest.TestCase):
    def test_access_nest_map(self):
        nested_map = {
            "a": {
                "b": {
                    "c": 1
                }
            }
        }

        result1 = access_nested_map(nested_map, ["a", "b", "c"])
        self.assertEqual(result1, 1)

        with self.assertRaises(KeyError):
            access_nested_map(nested_map, ["a", "x"])

        
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, ["a", "b", "x"])


        with self.assertRaises(KeyError):
            access_nested_map(nested_map, ["x"])


        result5 = access_nested_map(nested_map, [])
        self.assertEqual(result5, nested_map)


if __name__ == '__main__':
    unittest.main()