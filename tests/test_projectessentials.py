import os.path

def test_fileexist_license():
    assert os.path.isfile("LICENSE.md")

def test_fileexists_readme():
    assert os.path.isfile("README.md")
