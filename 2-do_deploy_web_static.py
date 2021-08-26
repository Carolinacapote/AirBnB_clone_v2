#!/usr/bin/python3
'''
Fabric script that generates a .tgz archive from the contents of the web_static
folder and distributes an archive to the web servers
'''
from fabric.api import *
from datetime import datetime
from os import path
env.hosts = ['34.138.154.248', '35.227.26.227']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/id_rsa'


def do_pack():
    '''Function that generates the .tgz archives '''
    # if versions folder does not exist
    local('mkdir -p versions/')

    date_time = datetime.now()
    str_date = date_time.strftime('%Y%m%d%H%M%S')
    archive_path = 'versions/web_static_' + str_date + '.tgz'

    # Generates the .tgz archive
    try:
        tar_file = local('tar -cvzf {} web_static/'.format(archive_path))
        return archive_path
    except:
        return None


def do_deploy(archive_path):
    ''' Function that distributes an archive to the web servers '''
    file_n = archive_path[9:-4]

    if path.exists(archive_path) is False:
        return False

    try:
        # Upload the archive to the /tmp/
        put(archive_path, '/tmp/')

        # Uncompress the archive on the web server
        run('sudo mkdir -p /data/web_static/releases/{}/'.format(file_n))
        pth = '/data/web_static/releases/{}/'.format(file_n)
        run('sudo tar -xzf /tmp/{}.tgz -C '.format(file_n) + pth)

        # Delete the archive from the web server
        run('sudo rm /tmp/{}.tgz'.format(file_n))

        # Move data
        # run('sudo mv ' + pth + 'web_static/* ' + pth)

        # Delete old path
        run('sudo rm -rf ' + pth + 'web_static')

        # Delete the symlink from the server
        run('sudo rm -rf /data/web_static/current')

        # Create a new symlink on the server
        run('sudo ln -sf ' + pth + ' /data/web_static/current')

    except:
        return False

    return True
