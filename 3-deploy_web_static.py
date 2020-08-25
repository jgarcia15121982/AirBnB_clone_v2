#!/usr/bin/python3
""" Generates a .tgz archive """


import os
from fabric.api import *
from datetime import datetime


def do_pack():
    """ generate a tgz file """
    time_f = '%Y%m%d%H%M%S'
    try:
        if not os.path.exists('versions'):
            local('mkdir versions')
        to = 'versions/web_static_{}.tgz'.format(
                datetime.now().strftime(time_f))

        local('tar -cvzf {} web_static'.format(to))
        return(to)
    except:
        return (None)


def do_deploy(archive_path):
    """ distributes an archive to a web server """
    if not os.path.exists(archive_path):
        return (False)

    try:
        put(archive_path, '/tmp/')
        t_file = archive_path.split('/')[1].split(t_file)
        w = '/data/web_static/releases/{}'.format(t_file)
        run('sudo mkdir -p {}'.format(w))
        run('tar -zxvf /tmp/{}.tgz -C {}/'.format(t_file, w))
        run('sudo rm /tmp/{}'.format(archive_path.split('/')[1]))
        run('sudo rm /data/web_static/current')
        run('sudo ln -sf /data/web_static/releases/{} \
        /data/web_static/current'.format(t_file))
        run('sudo mv /data/web_static/releases/{}/web_static/*\
        /data/web_static/releases/{}'.format(t_file, t_file))
        run('rm -rf /data/web_static/releases/{}/web_static/'.format(t_file))
        return (True)
    except:
        return (False)


def deploy():
    """ deploy """
    r_pack = do_pack()
    if r_pack is None:
        return (False)
    return (do_deploy(r_pack))
