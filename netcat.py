import argparse
import socket
import shlex
import subprocess
import sys
import textwrap
import threading

# this function receives a command, execute it, and return the output as a string
def execute(cmd):
    cmd = cmd.strip()
    if not cmd:
        return
    output = subprocess.check_output(shlex.split(cmd), stderr=subprocess.STDOUT)
    return output.decode()
    