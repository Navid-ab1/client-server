import zmq
import json

def send_request(command):
    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect('tcp://localhost:5555')
    socket.send_string(json.dumps(command))
    response = socket.recv_string()
    print(f'Response of the server is {response}')
    return response  # Return the response for testing purposes

if __name__ == '__main__':
    os_command = {
        "command_type": "os",
        "command": "ls",
        "args": ["-l"]
    }

    math_command = {
        "command_type": "math",
        "operation": "multiply",
        "operands": [5, 10]
    }

    ping_command = {
        "command_type": "os",
        "command": "ping",
        "args": ["-c", "4", "8.8.8.8"]  # "-c 4" means send 4 pings
    }

    print("Sending os command ")
    send_request(os_command)
    print("Sending math command")
    send_request(math_command)
    print("Sending ping command")
    send_request(ping_command)
