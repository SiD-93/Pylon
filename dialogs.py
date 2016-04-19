import subprocess, shlex

def make(dialogType, message) :
    base = 'zenity'
    command = base + ' --' + dialogType + ' --text="' + message + '"'
    args = shlex.split(command)
    subprocess.call(args)
