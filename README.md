# PyWAT - Python Windows Advanced Tools

**PyWAT** is a powerful Python library designed to provide advanced tools for interacting with the Windows operating system. It combines functionality similar to **PyWin32**, **psutil**, **os**, and **shutil**, allowing users to perform a wide range of operations on Windows environments.

## Features

- **File Management**: Copy, move, delete, and list files and directories.
- **System Monitoring**: Retrieve real-time CPU and memory usage, list active processes, and terminate processes.
- **Registry Operations**: Read and write Windows registry keys and values.
- **Command Execution**: Run commands in the Windows command prompt and capture their outputs.

## License

This project is licensed under the Custom License for PyWAT. See the [LICENSE](LICENSE) file for details.

### Key Restrictions:

- No modification or redistribution of the Software or modified versions.
- Redistribution of modified versions is strictly prohibited to avoid the introduction of malware.
- The Software is provided "as is" with no warranty of any kind.

## GitHub Repository

The PyWAT GitHub Repository Is:

https://github.com/NotVirusTotal/pywat

## Installation

You can install **PyWAT** via **pip** from the Python Package Index (PyPI):

```bash
pip install pywat
```

**Usage**
Once installed, you can import the library into your Python code and use its features. Here's a simple example:

```bash
import pywat as wat

# File Operations: Copy a file
wat.copy_file('source.txt', 'destination.txt')

# System Monitoring: Check CPU usage
cpu_usage = wat.cpu_usage()
print(f"Current CPU Usage: {cpu_usage}%")

# Run a command in the Windows Command Prompt
stdout, stderr = wat.run_cmd('dir')
print("Command Output:", stdout)
print("Command Error (if any):", stderr)
