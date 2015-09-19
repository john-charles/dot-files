#!/usr/bin/env python
import subprocess

if __name__ == '__main__':

    proc = subprocess.Popen(('df', '-h', '.'), stdout=subprocess.PIPE)
    output = proc.stdout.read()

    line = output.split('\n')[1]

    while line.count('  '):
        line = line.replace('  ', ' ')

    print(line.split(' ')[2])
    
