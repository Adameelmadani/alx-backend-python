#!/usr/bin/env python3
"""
This is our module
"""
import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
GithubOrgClient = __import__("client").GithubOrgClient
"""
These are testing modules
"""


class TestGithubOrgClient(unittest.TestCase):
    """
    Test class to test GithubOrgClient class
    """
    @parameterized.expand([
        ("google", {"name": "google"}),
        ("abc", {"name": "abc"})
        ])
    @patch("client.get_json")
    def test_org(self, org_name, org_json, get_mock):
        """
        Testing org function
        """
        get_mock.return_value = org_json
        test = GithubOrgClient(org_name)
        self.assertEqual(test.org, org_json)
        get_mock.assert_called_once()


if __name__ == "__main__":
    unittest.main()
