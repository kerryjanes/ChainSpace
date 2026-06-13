# test_chainspace.py
"""
Tests for ChainSpace module.
"""

import unittest
from chainspace import ChainSpace

class TestChainSpace(unittest.TestCase):
    """Test cases for ChainSpace class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = ChainSpace()
        self.assertIsInstance(instance, ChainSpace)
        
    def test_run_method(self):
        """Test the run method."""
        instance = ChainSpace()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
