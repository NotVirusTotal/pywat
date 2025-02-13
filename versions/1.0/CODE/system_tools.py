# pywat/system_tools.py
import psutil

def cpu_usage():
    """
    Returns the current CPU usage percentage.
    """
    return psutil.cpu_percent(interval=1)

def memory_usage():
    """
    Returns the current memory usage percentage.
    """
    return psutil.virtual_memory().percent

def get_active_processes():
    """
    Retrieves a list of active processes with their PID and name.
    """
    processes = []
    for proc in psutil.process_iter(['pid', 'name']):
        processes.append(proc.info)
    return processes

def terminate_process(pid):
    """
    Terminates the process with the given PID.
    """
    process = psutil.Process(pid)
    process.terminate()
