# pywat/cmd_tools.py
import subprocess

def run_cmd(command):
    """
    Executes the given command in the Windows command prompt and returns stdout and stderr.
    """
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    return result.stdout, result.stderr
