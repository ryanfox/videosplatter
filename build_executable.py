import os
import sys

import gooey
from cx_Freeze import setup, Executable


def get_resources():
    gooey_dir = os.path.dirname(gooey.__file__)
    includes = []
    for directory in ['languages', 'images']:
        path = os.path.join(gooey_dir, directory)
        for filename in os.listdir(path):
            file_path = os.path.join(path, filename)
            target_path = os.path.join('gooey', directory, filename)
            includes.append((file_path, target_path))
    
    return includes


# Dependencies are automatically detected, but it might need fine tuning.
# "packages": ["os"] is used as example only
build_exe_options = {
    'include_files': get_resources(),
    'excludes': ['tkinter',],
}

# base="Win32GUI" should be used only for Windows GUI app
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name = "Videosplatter",
    version = "0.3",
    description = "Splat a video into individual frames",
    options = {"build_exe": build_exe_options},
    executables = [Executable("videosplatter/gui.py", base=base)]
)

