"""Tests for dataset console script"""
import unittest
from scripts.dataset import parse_arguments


class TestParseArguments(unittest.TestCase):
    """Tests for dataset module"""

    def test_basic_with_defaults(self):
        """Test argument parsing logic"""
        args = parse_arguments(["install"])
        self.assertEqual("install", args.command)
        self.assertEqual("INFO", args.log_level)
        self.assertFalse(args.force)

    def test_no_arguments_is_invalid(self):
        """Test argument parsing logic"""
        self.assertRaises(SystemExit, parse_arguments, [])
