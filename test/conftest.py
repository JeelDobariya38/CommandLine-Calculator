# conftest.py
import sys
import os

file_path = os.path.dirname(__file__)
path = os.path.join(file_path, '..' + os.pathsep + 'src')
project_dir = os.path.abspath(path)

if project_dir not in sys.path:
    sys.path.insert(0, path)
    print("Resolveing Paths......")
