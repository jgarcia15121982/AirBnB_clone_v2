#!/usr/bin/python3
""" Generates a .tgz archive """


from fabric.api import *
from datetime import datetime
import os


def do_pack():
    """ generate a tgz file """
    time_f = '%Y%m%d%H%M%S'
    try:
        if os.path.versions not exists:
            local(mkdir versions)
            to = 'version/web_static_{}.tgz'.format(datetime.now().strftime(time_f))

            local('tar -cvzf {} web_static'.format(to))
            return(to)
    except:
        return (None)

