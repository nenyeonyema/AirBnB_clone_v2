#!/usr/bin/python3
"""Fabric script that distributes an archive to your web servers."""

from fabric.api import env, put, run
from os.path import exists
from datetime import datetime

env.hosts = ["100.25.152.48", "100.27.13.220"]
env.user = 'ubuntu'


def do_deploy(archive_path):
    """Distributes an archive to the web servers."""
    if not exists(archive_path):
        return False

    try:
        # Upload archive to /tmp directory on the server
        put(archive_path, '/tmp')

        # Create directory for the archive
        archive_name = archive_path.split('/')[-1]
        archive_folder = archive_name.split('.')[0]
        release_path = '/data/web_static/releases/' + archive_folder + '/'

        run('mkdir -p {}'.format(release_path))

        # Uncompress the archive
        run('tar -xzf /tmp/{} -C {}'.format(archive_name, release_path))

        # Remove the archive from the server
        run('rm /tmp/{}'.format(archive_name))

        # Move the files to appropriate directory
        run('mv {}web_static/* {}'.format(release_path, release_path))

        # Remove the symbolic link /data/web_static/current
        run('rm -rf /data/web_static/current')

        # Create new symbolic link
        run('ln -s {} /data/web_static/current'.format(release_path))

        print('New version deployed!')
        return True
    except Exception as e:
        return False
