#!/usr/bin/env python3
"""
This is our python module
"""
from parameterized import parameterized
import unittest
access_nested_map = __import__("utils").access_nested_map
"""
These are testing modules
"""


class TestAccessNestedMap(unittest.TestCase):
    """
    This is our test class
    """
    @parameterized.expand([
        ({"nm": {"a": 1}, "p": ("a",)}, 1),
        ({"nm": {"a": {"b": 2}}, "p": ("a",)}, {"b": 2}),
        ({"nm": {"a": {"b": 2}}, "p": ("a", "b")}, 2)
        ])
    def test_access_nested_map(self, input, expected):
        """This function tests access_nested_map function"""
        self.assertEqual(access_nested_map(input["nm"], input["p"]), expected)

    @parameterized.expand([
        ({"nm": {}, "p": ("a",), "key": "\'a\'"}, 2),
        ({"nm": {"a": 1}, "p": ("a", "b"), "key": "\'b\'"}, 2)
        ])
    def test_access_nested_map_exception(self, input, expected):
        """This function tests access_ensted_map() if it raises exceptions"""
        with self.assertRaises(KeyError) as e:
            access_nested_map(input["nm"], input["p"])
        self.assertEqual(str(e.exception), input["key"])


if __name__ == "__main__":
    unittest.main()
