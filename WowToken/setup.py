from cx_Freeze import setup, Executable
import os
import tkinter

base = None    

executables = [Executable("ImportToken.py", base=base)]

additional_mods = ['numpy.core._methods', 'numpy.lib.format']
packages = ["urllib.request","gzip","json","matplotlib","datetime",'tkinter','os']
options = {
    'build_exe': {    
        'packages':packages,
        'includes':additional_mods,
        'include_files':[r"C:\Users\David\AppData\Local\Programs\Python\Python36-32\DLLs\tcl86t.dll", 
                         r"C:\Users\David\AppData\Local\Programs\Python\Python36-32\DLLs\tk86t.dll"]
    },    
}

os.environ['TCL_LIBRARY'] = r'C:\Users\David\AppData\Local\Programs\Python\Python36-32\tcl\tcl8.6'
os.environ['TK_LIBRARY'] = r'C:\Users\David\AppData\Local\Programs\Python\Python36-32\tcl\tk8.6'

setup(
    name = "WOWToken",
    options = options,
    version = "1",
    description = 'jejejejej',
    executables = executables
)