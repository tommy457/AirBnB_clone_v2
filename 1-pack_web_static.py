#!/usr/bin/python3
"""Module for packing web static"""
from datetime import datetime
from fabric.api import local


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
