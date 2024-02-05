#!/usr/bin/env python3
"""
This is our python module
"""
from parameterized import parameterized, parameterized_class
import unittest
from unittest.mock import patch, Mock
access_nested_map = __import__("utils").access_nested_map
get_json = __import__("utils").get_json
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


@parameterized_class(("input", "expected"), [
    ({"test_url": "http://example.com", "test_payload": {"payload": True}},
        {"payload": True}),
    ({"test_url": "http://holberton.io", "test_payload": {"payload": False}},
        {"payload": False})
    ])
class TestGetJson(unittest.TestCase):
    """
    This class tests getjson function
    """
    @patch("utils.requests.get")
    def test_get_json(self, get_mock):
        """Tests utils.get_json function"""
        get_mock.json.return_value = self.input["test_payload"]
        self.assertEqual(get_mock.json(self.input["test_url"]), self.expected)
        get_mock.json.assert_called_once()


if __name__ == "__main__":
    unittest.main()
