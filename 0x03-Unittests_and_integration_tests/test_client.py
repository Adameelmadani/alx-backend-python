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

    def test_public_repos_url(self):
        """
        Testing public_repos_url function
        """
        test = GithubOrgClient("url")
        with patch("client.GithubOrgClient.org") as get_mock:
            with patch("client.GithubOrgClient._public_repos_url") as get_m2:
                get_mock.return_value = {"repos_url": "google"}
                get_m2.return_value = get_mock.return_value["repos_url"]
                self.assertEqual(test._public_repos_url, "google")


if __name__ == "__main__":
    unittest.main()
