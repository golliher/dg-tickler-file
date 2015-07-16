#!/usr/bin/env python
import unittest
import os.path

class TestLicenseExists(unittest.TestCase):

    def test_fileexist_license(self):
        self.assertTrue(os.path.isfile("LICENSE.md"))

if __name__ == "__main__":
    unittest.main()
