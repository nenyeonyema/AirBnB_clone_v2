#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive from the contents of the
web_static folder of your AirBnB Clone repo
"""

from fabric.api import local
from datetime import datetime


def do_pack():
    """
    Generates a .tgz archive from the contents of the web_static folder
    """
    local("mkdir -p versions")
    date_time = datetime.utcnow().strftime("%Y%m%d%H%M%S")
    file_path = "versions/web_static_{}.tgz".format(date_time)
    result = local("tar -cvzf {} web_static".format(file_path))
    if result.failed:
        return None
    return file_path
