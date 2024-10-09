import pytest
from client import send_request
from unittest.mock import Mock

def test_send_request_os_command(mocker):
    # Mock the zmq Context and socket
    mock_context = mocker.patch('client.zmq.Context')
    mock_socket = Mock()
    mock_context.return_value.socket.return_value = mock_socket

    # Set the return value for recv_string
    mock_socket.recv_string.return_value = 'mocked os response'

    os_command = {
        "command_type": "os",
        "command": "ls",
        "args": ["-l"]
    }

    response = send_request(os_command)

    mock_socket.send_string.assert_called_with('{"command_type": "os", "command": "ls", "args": ["-l"]}')
    mock_socket.recv_string.assert_called_once()
    assert response == 'mocked os response'

def test_send_request_math_command(mocker):

    mock_context = mocker.patch('client.zmq.Context')
    mock_socket = Mock()
    mock_context.return_value.socket.return_value = mock_socket

   
    mock_socket.recv_string.return_value = '50'

    math_command = {
        "command_type": "math",
        "operation": "multiply",
        "operands": [5, 10]
    }

    response = send_request(math_command)

    mock_socket.send_string.assert_called_with('{"command_type": "math", "operation": "multiply", "operands": [5, 10]}')
    mock_socket.recv_string.assert_called_once()
    assert response == '50'
