import zmq
import subprocess
import json

def os_command(command, args):
    try:
        result = subprocess.run([command] + args, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=10)
        if result.returncode == 0:
            return result.stdout.decode()
        else:
            return result.stderr.decode()
    except Exception as e:
        return f"console error: {str(e)}"

def execute_math(operation, operand):
    try:
        if operation == 'sum':
            return sum(operand)
        elif operation == 'subtract':
            return operand[0] - operand[1]
        elif operation == 'divide':
            if operand[1] == 0:
                return "Error: division by zero"
            result = operand[0] / operand[1]
            return result
        elif operation == 'multiply':
            result = 1
            for num in operand:
                result *= num
            return result
        else:
            return "Error: An unsupported operation occurred"
    except Exception as e:
        return f"console error: {str(e)}"

def run_server():
    context = zmq.Context()
    socket = context.socket(zmq.REP)  # REP socket for replies
    socket.bind("tcp://*:5555")  # Bind the server to port 5555
    print('Server is running ... Waiting for requests')

    while True:
        message = socket.recv_string()
        print(f"Received message {message}")

        command = json.loads(message)
        print(command, 'the form of the command is like')

        if command['command_type'] == 'os':
            result = os_command(command['command'], command['args'])
        elif command['command_type'] == 'math':
            result = execute_math(command['operation'], command['operands'])
        else:
            result = 'Error: Unknown command type'


        socket.send_string(str(result)) 

if __name__ == '__main__':
    run_server()
