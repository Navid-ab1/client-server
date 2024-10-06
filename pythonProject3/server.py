import zmq
import subprocess
import json

def os_command(command,args):
    try:
        result = subprocess.run([command]+args,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
        return result.stdout.decode() if result.returncode == 0 else result.stderr.decode() 
    except Exception as e:
        return f"console error{str(e)}"
    
def execute_math(operation,operand):
    try:
        if operation =='sum':
            return sum(operand)    
        elif operation =='subract':
            return (operand[0]-operand[1])
        elif operation =='divide':
            return operand[0]/operand[1] if operand[1]!='0' else "Error:division by zero"
        elif operation =='muliply':
            res = 1
            for num in operand:
                res *=num
            return res
        else: return "Error:An unsupported operation occured"
    except Exception as e:
        return f"console error{str(e)}"
    

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")
print('server is running ... Waiting for requests')



while True:
    message = socket.recv_string
    print(f"receved message {message}")
    command = json.loads(message)
    print(command ,f'the form of the command is like')
    if command['command_type'] =='os':
        result = os_command(command['command'],command['args'])
    elif command['command_type'] == 'math':
        result = execute_math(command['command'],command['args'])
    else: result ='Error: has happened'

    socket.send_string(result)
