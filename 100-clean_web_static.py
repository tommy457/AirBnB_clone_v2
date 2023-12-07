#!/usr/bin/python3
"""Cleaning  out-of-date archives"""

from fabric.api import *
import os


env.hosts = ['54.236.24.86', '18.233.63.71']


def do_clean(number=0):
    """Deletes out-of-date archives"""
    if int(number) == 0:
        idx = 1
    else:
        idx = int(number)

    paths = sorted(os.listdir("versions"))
    with lcd("versions"):
        if idx < len(paths):
            for file_ in paths[:-idx]:
                local("rm ./{}".format(file_))

    with cd("/data/web_static/releases"):
        paths = run("ls -tr").split()
        files = []
        for file_ in paths:
            if "web_static_" in file_:
                files.append(file_)
        if idx < len(files):
            for file_ in files[idx:]:
                run("rm -rf ./{}".format(file_))
