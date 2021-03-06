import pytest
from mock import patch, MagicMock

from open_folder import *

def test_folder_exists():
    with patch('subprocess.check_call', MagicMock(return_value="NOOP")):
        result = open_folder(".")
        assert result == None

def test_folder_does_not_exists():
    with patch('subprocess.check_call', MagicMock(return_value="NOOP")):
        with pytest.raises(Exception) as excinfo:
            open_folder("it_is_very_unlikely_that_this_file_exists_20150718")
        assert str(excinfo.value) == ('Folder does not exist.')

def test_unsupported_os():
    with patch('subprocess.check_call', MagicMock(return_value="NOOP")):

        with patch('platform.system', MagicMock(return_value="NotDarwinWindowsLinux")):
            with pytest.raises(Exception) as excinfo:
                open_folder("/")
            assert str(excinfo.value).startswith('Your operating system was not recognized.')

def test_supported_os():
    with patch('subprocess.check_call', MagicMock(return_value="NOOP")):

        with patch('platform.system', MagicMock(return_value="Linux")):
            result = open_folder("/")
            assert result == None
        with patch('platform.system', MagicMock(return_value="Darwin")):
            result = open_folder("/")
            assert result == None
        with patch('platform.system', MagicMock(return_value="Windows")):
            result = open_folder("/")
            assert result == None
