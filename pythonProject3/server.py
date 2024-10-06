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
    if operation =='sum':
        return sum(operand)    
    