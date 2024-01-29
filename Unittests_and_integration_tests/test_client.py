#!/usr/bin/env python3
"""unit tests for utils"""
import unittest
from unittest import TestCase, mock
from unittest.mock import patch, Mock
from parameterized import parameterized
from client import GithubOrgClient

class TestGithubOrgClient(unittest.TestCase):
    """unit test for githuborgclient from client.py"""
    @parameterized.expand([
        ("google"),
        ("abc"),
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        """testing that githuborgclient returns the expected result"""
        github_org_client = GithubOrgClient(org_name)

        github_org_client.org

        mock_get_json.assert_called_once_with(
            f'https://api.github.com/orgs/{org_name}')


if __name__ == '__main__':
    unittest.main()
