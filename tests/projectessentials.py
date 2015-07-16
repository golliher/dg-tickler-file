#!/usr/bin/env python
import unittest
import os.path

class TestLicenseExists(unittest.TestCase):

    def test_fileexist_license(self):
        self.assertTrue(os.path.isfile("LICENSE.md"))

class TestReadmeExists(unittest.TestCase):
    def test_fileexists_readme(self):
        self.assertTrue(os.path.isfile("README.md"))

if __name__ == "__main__":
    unittest.main()
