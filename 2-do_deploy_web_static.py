#!/usr/bin/python3
"""Module to deploy an archive"""
from fabric.api import put, run, env
from os.path import isfile
from fabric import task

env.hosts = ['54.236.24.86', '18.233.63.71']


@task
def do_deploy(archive_path):
    """Distributes an archive to your web servers"""

    if not isfile(archive_path):
        return False

    file_name_with_ext = archive_path.split("/")[-1]
    file_name = file_name_with_ext.split(".")[0]

    task_1 = put(archive_path, "/tmp/")
    if task_1.failed:
        return False

    task_2 = run("mkdir -p /data/web_static/releases/{}".format(file_name))
    if task_2.failed:
        return False

    task_3 = run("tar -xzf /tmp/{} -C /data/web_static/releases/{}".
                 format(file_name_with_ext, file_name))
    if task_3.failed:
        return False

    task_4 = run("rm -fr /tmp/{}".format(file_name_with_ext))
    if task_4.failed:
        return False

    task_5 = run("rm -f /data/web_static/current")
    if task_5.failed:
        return False

    task_6 = run("ln -s /data/web_static/current /data/web_static/releases/{}"
                 .format(file_name))
    if task_6.failed:
        return False

    return True
