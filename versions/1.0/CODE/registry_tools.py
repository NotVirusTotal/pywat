# pywat/registry_tools.py
import winreg

def read_registry(key):
    """
    Reads a registry value from HKEY_LOCAL_MACHINE using the specified key.
    """
    with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, key) as reg_key:
        value, _ = winreg.QueryValueEx(reg_key, 'MyValue')
        return value

def write_registry(key, value):
    """
    Writes a value to the registry at HKEY_LOCAL_MACHINE for the specified key.
    """
    with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, key, 0, winreg.KEY_SET_VALUE) as reg_key:
        winreg.SetValueEx(reg_key, 'MyValue', 0, winreg.REG_SZ, value)
