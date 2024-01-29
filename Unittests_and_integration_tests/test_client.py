#!/usr/bin/env python3
"""unit tests for utils"""
import unittest
import fixtures
from fixtures import TEST_PAYLOAD
from unittest import TestCase, mock
from unittest.mock import patch, Mock, PropertyMock
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

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        """test that public repos returns expected result"""
        mock_repos_payload = [{'name': 'repo1'}, {'name': 'repo2'}]
        mock_get_json.return_value = mock_repos_payload
        mock_public_repos_url = 'http://mocked.url/repos'

        with patch.object(GithubOrgClient,
                          'public_repos_url',
                          new_callable=PropertyMock) as mock_repo_url:
            mock_repo_url.return_value = mock_public_repos_url

            github_org_client = GithubOrgClient("some_org")

            public_repos = github_org_client.public_repos()

            self.assertEqual(public_repos,
                             [repo['name'] for repo in mock_repos_payload])

            mock_repo_url.assert_called_once()
            mock_get_json.assert_called_once_with(mock_public_repos_url)

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, 'my_license', True),
        ({"license": {"key": "other_license"}}, 'my_license', False),
    ])
    def test_has_license(self, repo, license_key, expected):
        """ Test that GithubOrgClient.has_license returns the correct value.
        """
        github_org_client = GithubOrgClient("some_org")

        has_license = github_org_client.has_license(repo, license_key)

        self.assertEqual(has_license, expected)


@parameterized_class(
    ("org_payload", "repos_payload", "expected_repos", "apache2_repos"),
    fixtures.TEST_PAYLOAD)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """ Test for the GithubOrgClient class.
        Args:
            unittest (unittest.TestCase): unittest
    """
    @classmethod
    def setUpClass(cls):
        """ Test for the GithubOrgClient class.
            Args:
                unittest (unittest.TestCase): unittest
        """
        # Start the patcher for requests.get
        cls.get_patcher = patch('requests.get')
        cls.mock_get = cls.get_patcher.start()

        # Define the side_effect function for your mock
        def side_effect(url):
            if url == f"https://api.github.com/orgs/ \
                    {cls.org_payload['login']}":
                return Mock(json=lambda: cls.org_payload)
            elif url == f"https://api.github.com/orgs/ \
                    {cls.org_payload['login']}/repos":
                return Mock(json=lambda: cls.repos_payload)
            # ... handle other URLs if necessary ...
            return Mock(status_code=404)

        cls.mock_get.side_effect = side_effect

    @classmethod
    def tearDownClass(cls):
        """ Test for the GithubOrgClient class.
            Args:
                unittest (unittest.TestCase): unittest
        """
        # End the patch
        cls.get_patcher.stop()

    def test_public_repos(self):
        """ Test that GithubOrgClient.public_repos returns the expected result
        """
        github_org_client = GithubOrgClient("google")

        self.get_patcher = patch('client.get_json',
                                 return_value=self.repos_payload)

        self.mock_get_json = self.get_patcher.start()

        repos = github_org_client.public_repos()

        self.assertEqual(repos, self.expected_repos)

        self.mock_get_json.assert_called_once()

        self.get_patcher.stop()


if __name__ == '__main__':
    unittest.main()
