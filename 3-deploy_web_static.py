#!/usr/bin/python3
"""Fabric script that creates and distributes an archive to web servers."""

from fabric.api import env, local, put, run
from datetime import datetime
import os

env.hosts = ['54.152.245.111', '54.227.196.221']
env.user = 'ubuntu'


def do_pack():
    """Creates an archive from the web_static folder."""
    try:
        now = datetime.now().strftime('%Y%m%d%H%M%S')
        archive_path = 'versions/web_static_{}.tgz'.format(now)
        local('mkdir -p versions')
        local('tar -cvzf {} web_static'.format(archive_path))
        return archive_path
    except:
        return None

def do_pack():
    """Creates an archive from the web_static folder."""
    try:
        now = datetime.now().strftime('%Y%m%d%H%M%S')
        archive_path = 'versions/web_static_{}.tgz'.format(now)
        local('mkdir -p versions')
        local('tar -cvzf {} web_static'.format(archive_path))
        return archive_path
    except Exception as e:  # Catch specific exception
        return None


def do_deploy(archive_path):
    """Distributes an archive to the web servers."""
    if not os.path.exists(archive_path):
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
    except Exception as e:  # Catch specific exception
        return False
