#!/usr/bin/python3
""" 
Fabric script that generates a .tgz archive
from the contents of the web_static folder 
"""
from fabric.api import local
from datetime import datetime
import os


def do_pack():
    """ Packs web_static files into .tgz format """
    try:
        if not os.path.exists("versions"):
            os.makedirs("versions")

        current_time = datetime.now().strftime("%Y%m%d%H%M%S")
        file_name = "versions/web_static_" + current_time + ".tgz"

        local("tar -cvzf {} web_static".format(file_name))

        return file_name
    except Exception as e:
        return None
