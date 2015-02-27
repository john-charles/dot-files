__author__ = 'john-charles'

import shutil


def copy_file(src, dst):
    # Eventually I might want to change how I copy a file.
    shutil.copy(src, dst)
