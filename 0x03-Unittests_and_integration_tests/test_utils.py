#!/usr/bin/env python3
"""Unittest for access_nested_map function
"""
import unittest
from utils import access_nested_map, get_json, memoize
from typing import Mapping, Sequence, Any
from parameterized import parameterized
from unittest.mock import patch, Mock


class TestAccessNestedMap(unittest.TestCase):
    """Test class for access_nested_map function
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(
            self, nested_map: Mapping, path: Sequence, expected: Any):
        """Tests the access_nested_map function
        """
        result = access_nested_map(nested_map, path)
        self.assertEqual(result, expected)

    @parameterized.expand([
        ({}, ("a",), 'a'),
        ({"a": 1}, ("a", "b"), 'b')
    ])
    def test_access_nested_map_exception(self, nested_map,  path, expected):
        """Tests that a KeyError is raised for given inputs
        """
        with self.assertRaises(KeyError) as e:
            access_nested_map(nested_map, path)
        self.assertEqual(f"KeyError('{expected}')", repr(e.exception))


class TestGetJson(unittest.TestCase):
    """Test class for get_json function
    """

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url, test_payload):
        """ Test get_json returns the expected results
        """
        mock = Mock()
        mock.json.return_value = test_payload
        with patch("utils.requests.get", return_value=mock) as mock_request:
            result = get_json(test_url)
            mock_request.assert_called_once_with(test_url)
            self.assertEqual(result, test_payload)


if __name__ == "__main__":
    unittest.main()
