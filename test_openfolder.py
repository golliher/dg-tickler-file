import pytest
from mock import patch, MagicMock

from open_folder import *

def test_folder_exists():
    with patch('subprocess.check_call', MagicMock(return_value="NOOP")):
        open_folder(".")

def test_folder_does_not_exists():
    with patch('subprocess.check_call', MagicMock(return_value="NOOP")):
        with pytest.raises(Exception):
            open_folder("it_is_very_unlikely_that_this_file_exists_20150718")

def test_unsupported_os():
    with patch('subprocess.check_call', MagicMock(return_value="NOOP")):
        with patch('platform.system', MagicMock(return_value="NotDarwinWindowsLinux")):
            with pytest.raises(Exception):
                open_folder("/")

def test_supported_os():
    with patch('subprocess.check_call', MagicMock(return_value="NOOP")):

        with patch('platform.system', MagicMock(return_value="Linux")):
            open_folder("/")
        with patch('platform.system', MagicMock(return_value="Darwin")):
            open_folder("/")
        with patch('platform.system', MagicMock(return_value="Windows")):
            open_folder("/")
