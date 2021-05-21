import sys
from cx_Freeze import setup, Executable
base = None
if (sys.platform == "win32"):

        base = "Win32GUI"  
        setup(name="myprogram",
                version="0.1",
                description="myfirst program",
                executables=[Executable("mysoftware.pyw",base=base)]
        )