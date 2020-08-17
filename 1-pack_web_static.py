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
            
        to = 'versions/web_static_{}.tgz'.format(datetime.now().strftime(time_f))

        local('tar -cvzf {} web_static'.format(to))
        return(to)
    except:
        return (None)
