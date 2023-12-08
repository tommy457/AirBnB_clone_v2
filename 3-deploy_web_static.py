#!/usr/bin/python3
"""Full deployment"""
from fabric.api import *
from os.path import exists
from datetime import datetime


env.hosts = ['54.236.24.86', '18.233.63.71']


def deploy():
    """Creates and distributes an archive to web servers"""
    archive_path = do_pack()
    if archive_path:
        return do_deploy(archive_path)
    return False


def do_pack():
    """Creates an archive file from the the web_static folder"""
    local("mkdir -p versions")
    birth_date = datetime.now().strftime("%Y%m%d%H%m%S")
    file_name = "web_static_" + birth_date
    output_file = "versions/{}.tgz".format(file_name)
    result = local("tar -cvzf {} web_static".format(output_file))
    if result.succeeded:
        return output_file
    return None


def do_deploy(archive_path):
    """Distributes an archive to your web servers"""

    try:
        if not exists(archive_path):
            return False

        file_name_with_ext = archive_path.split("/")[-1]
        file_name = file_name_with_ext.split(".")[0]

        put(archive_path, "/tmp/")

        run("mkdir -p /data/web_static/releases/{}/".format(file_name))

        run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/".format(
            file_name_with_ext, file_name))

        run("rm /tmp/{}".format(file_name_with_ext))

        run('mv /data/web_static/releases/{}/web_static/* \
                /data/web_static/releases/{}/'.format(file_name, file_name))

        run("rm -rf /data/web_static/releases/{}/web_static".format(
            file_name))

        run("rm -rf /data/web_static/current")

        run("ln -s /data/web_static/releases/{}/ /data/web_static/current".format(
            file_name))

        return True

    except Exception:
        return False
