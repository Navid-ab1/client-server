import pytest
from server import os_command, execute_math
from unittest.mock import Mock

def test_os_command_valid(mocker):
    mock_subprocess = mocker.patch('subprocess.run')
    mock_result = Mock()
    mock_result.returncode = 0
    mock_result.stdout.decode.return_value = 'mocked output'
    mock_result.stderr.decode.return_value = ''
    mock_subprocess.return_value = mock_result

    result = os_command('ls', ['-l'])
    assert result == 'mocked output'

def test_os_command_invalid(mocker):
    mock_subprocess = mocker.patch('subprocess.run')
    mock_result = Mock()
    mock_result.returncode = 1
    mock_result.stdout.decode.return_value = ''
    mock_result.stderr.decode.return_value = 'mocked error'
    mock_subprocess.return_value = mock_result

    result = os_command('invalid command', [])
    assert result == 'mocked error'

def test_os_command_exception(mocker):
    mocker.patch('subprocess.run', side_effect=Exception('mocked exception'))
    result = os_command('ls', ['-l'])
    assert result == 'console error: mocked exception'

def test_execute_math_sum():
    result = execute_math('sum', [5, 10])
    assert result == 15

def test_execute_math_subtract():
    result = execute_math('subtract', [10, 5])
    assert result == 5

def test_execute_math_divide():
    result = execute_math('divide', [20, 5])
    assert result == 4.0

def test_execute_math_divide_by_zero():
    result = execute_math('divide', [10, 0])
    assert result == "Error: division by zero"
