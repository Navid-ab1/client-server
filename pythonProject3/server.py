import zmq
import subprocess
import json

def os_command(command, args):
    try:
        result = subprocess.run([command] + args, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,timeout=10)
        return result.stdout.decode() if result.returncode == 0 else result.stderr.decode()
    except Exception as e:
        return f"console error: {str(e)}"

def execute_math(operation, operand):
    try:
        if operation == 'sum':
            return sum(operand)
        elif operation == 'subtract':
            return operand[0] - operand[1]
        elif operation == 'divide':
            return operand[0] / operand[1] if operand[1] != 0 else "Error: division by zero"
        elif operation == 'multiply':  # Fixed typo
            result = 1
            for num in operand:
                result *= num
            return result
        else:
            return "Error: An unsupported operation occurred"
    except Exception as e:
        return f"console error: {str(e)}"

context = zmq.Context()
socket = context.socket(zmq.REP)  # REP socket for replies
socket.bind("tcp://*:5555")  # Bind the server to port 5555
print('Server is running ... Waiting for requests')

while True:
    message = socket.recv_string()
    print(f"Received message {message}")
    
    # Parse the JSON message from the client
    command = json.loads(message)
    print(command, 'the form of the command is like')
    
    # Handle the command based on its type
    if command['command_type'] == 'os':
        result = os_command(command['command'], command['args'])
    elif command['command_type'] == 'math':
        result = execute_math(command['operation'], command['operands'])
    else:
        result = 'Error: Unknown command type'

    # Send the result back to the client, ensuring it's a string
    socket.send_string(str(result))  # Ensure result is a string
