from cx_Freeze import setup, Executable
setup(name="myprogram",
        version="0.1",
        description="myfirst program",
        executables=[Executable("musicplayer.py" , base = "Win32GUI")]
)