import zmq
import json

context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect('tcp://localhost:5555')

def send_request(command):
    socket.send_string(json.dumps(command))
    response = socket.recv_string()
    print(f'Response of the server is {response}')


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
print("Sending os command")
send_request(ping_command)

