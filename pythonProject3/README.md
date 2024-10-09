## Project Structure

```plaintext
.
├── server.py        # The server that listens for client requests and processes commands
├── client.py        # The client that sends requests to the server and receives responses
├── test_server.py   # Unit tests for the server's functions (os_command, execute_math)
├── test_client.py   # Unit tests for the client's communication with the server
└── README.md        # Project documentation
```

## Prerequisites

To run this project, you will need the following:
- **Python 3.x**
- **ZeroMQ**: The project uses ZeroMQ for client-server communication.
- **pytest**: A Python testing framework used for unit tests.
- **pytest-mock**: A plugin for `pytest` to easily mock external dependencies.

To install the necessary Python libraries, run:

```bash
pip install pyzmq pytest pytest-mock
```

## How It Works

### Server (`server.py`)
The server listens on port `5555` using ZeroMQ and accepts JSON-encoded requests from the client. It supports two types of commands:

1. **OS Commands**:
   The server can run OS-level commands like `ls`, `pwd`, or `ping` via the `subprocess` module.
   
   Example request:
   ```json
   {
       "command_type": "os",
       "command": "ls",
       "args": ["-l"]
   }
   ```

2. **Math Operations**:
   The server can perform simple math operations like `sum`, `subtract`, `multiply`, and `divide`.

   Example request:
   ```json
   {
       "command_type": "math",
       "operation": "multiply",
       "operands": [5, 10]
   }
   ```

### Client (`client.py`)
The client sends requests to the server and displays the response received from the server.

#### Example Requests
- **OS Command**: Sends an `ls -l` command to the server.
- **Math Operation**: Sends a request to multiply `5` and `10`.
- **Ping Command**: Sends a ping request (`ping -c 4 8.8.8.8`) to the server.

The client prints the server's response to the console.

## How to Run the Project

1. **Start the Server**:
   First, you need to run the server, which will listen for incoming requests.
   ```bash
   python server.py
   ```

   The server will start and listen on port `5555` for incoming requests.

2. **Run the Client**:
   Once the server is running, you can run the client to send commands to the server.
   ```bash
   python client.py
   ```


## Running Tests

The project includes **unit tests** for both the server and client using `pytest`. The tests use mocking to simulate external dependencies such as subprocess calls and ZeroMQ sockets, allowing isolated testing of functionality.

### Run All Tests
To run the tests, simply use:

```bash
pytest
```

This will execute all tests in both `test_server.py` and `test_client.py`.

### Test Breakdown
- **`test_server.py`**: Contains unit tests for the server's `os_command` and `execute_math` functions. These tests mock the `subprocess.run` calls to avoid running actual system commands during testing.
- **`test_client.py`**: Contains unit tests for the client's interaction with the server. These tests mock the ZeroMQ socket to simulate sending requests and receiving responses without requiring a live server.

You can also run specific test files:

```bash
pytest test_server.py
```

Or run a specific test case:

```bash
pytest test_server.py::test_os_command_valid
```

