#!/usr/bin/python3
"""Module to deploy an archive"""
from fabric.api import put, run, env
from os.path import isfile

env.hosts = ['54.236.24.86', '18.233.63.71']


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

    task_4 = run("rm -rf /tmp/{}".format(file_name_with_ext))
    if task_4.failed:
        return False

    task7 = run('mv /data/web_static/releases/{}/web_static/* /data/web_static/releases/{}/'
            .format(file_name, file_name))
    if task7.failed:
        return False

    result = run("rm -rf /data/web_static/releases/{}/web_static".format(
        file_name))

    task_5 = run("rm -rf /data/web_static/current")
    if task_5.failed:
        return False

    task_6 = run("ln -s /data/web_static/releases/{} /data/web_static/current"
                 .format(file_name))
    if task_6.failed:
        return False

    return True
