#!/usr/bin/python3
"""Module to deploy an archive"""
from fabric.api import *
from os.path import exists

env.hosts = ['54.236.24.86', '18.233.63.71']


def do_deploy(archive_path):
    """Distributes an archive to your web servers"""

    try:
        if not exists(archive_path):
            return False

        file_name_with_ext = archive_path.split("/")[-1]
        file_name = file_name_with_ext.split(".")[0]

        put(archive_path, "/tmp/")

        run("mkdir -p /data/web_static/releases/{}".format(file_name))

        run("tar -xzf /tmp/{} -C /data/web_static/releases/{}".format(
            file_name_with_ext, file_name))

        run("rm /tmp/{}".format(file_name_with_ext))

        run('mv /data/web_static/releases/{}/web_static/* \
                /data/web_static/releases/{}/'.format(file_name, file_name))

        run("rm -rf /data/web_static/releases/{}/web_static".format(
            file_name))

        run("rm -rf /data/web_static/current")

        run("ln -s /data/web_static/releases/{} /data/web_static/current".
            format(file_name))

        return True

    except Exception:
        return False
