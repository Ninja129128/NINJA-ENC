import os, sys
os.system("git pull")
try:
    __import__("my_tool").ninja()
except Exception as e:
    exit(str(e))