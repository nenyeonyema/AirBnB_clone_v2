#!/usr/bin/python3
"""
Fabric script that deletes out-of-date archives.
"""

from fabric.api import env, run, lcd, cd
from datetime import datetime
import os

env.hosts = ['54.152.245.111', '54.227.196.221']
env.user = 'ubuntu'


def do_clean(number=0):
    """
    Deletes out-of-date archives.
    """
    try:
        number = int(number)
        if number < 0:
            number = 0

        # Local clean
        with lcd("versions"):
            local_archives = sorted(os.listdir('.'))
            to_delete = local_archives[:-number] \
                    if number > 0 else local_archives[:-1]
            for archive in to_delete:
                local("rm -f {}".format(archive))

        # Remote clean
        with cd("/data/web_static/releases"):
            remote_archives = run("ls -tr").split()
            to_delete = remote_archives[:-number] \
                    if number > 0 else remote_archives[:-1]
            for archive in to_delete:
                run("rm -f {}".format(archive))
    except Exception as e:
        pass
