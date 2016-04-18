import subprocess, shlex

def make(dialogType, message) :
    base = 'zenity'
    command = base + ' --' + dialogType + ' --text="' + message + '"'
    #print command
    args = shlex.split(command)
    subprocess.call(args)
