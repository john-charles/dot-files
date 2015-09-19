#!/usr/bin/env python
import subprocess

if __name__ == '__main__':

    proc = subprocess.Popen(('df', '-hT', '.'), stdout=subprocess.PIPE)
    output = proc.stdout.read()

    line = output.split('\n')[1]

    while line.count('  '):
        line = line.replace('  ', ' ')
    
    parts = line.split(' ')
    print("(%s)  %s free" % (parts[1], parts[4]))
    
