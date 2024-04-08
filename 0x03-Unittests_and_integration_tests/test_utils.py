#!/usr/bin/env python3
"""Unittest for access_nested_map function
"""
import unittest
from utils import access_nested_map
from parameterized import parameterized
from typing import Mapping, Sequence, Any


class TestAccessNestedMap(unittest.TestCase):
    """Test class fro access_nested_map function
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


if __name__ == "__main__":
    unittest.main()
