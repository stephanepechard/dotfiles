#!/usr/bin/python
# -*- coding: utf-8 -*-
""" dotfiles installation script.
    Created by Stéphane Péchard on 2012-07-23. """

# system
import getpass
import os
from subprocess import call


def install():
    """ Do everything. """
    clone_omz()
    clone_solarized()
    link_files()
    link_config()


def clone_omz():
    """ Get oh-my-zsh code. """
    call(['git', 'clone',
    'git://github.com/robbyrussell/oh-my-zsh.git', 'files/oh-my-zsh'])


def clone_solarized():
    """ Get Solarized code. """
    call(['git', 'clone',
    'git://github.com/altercation/solarized.git', 'solarized'])


def link_files():
    """ Create symbolic links to everything in the files directory. """
    username = getpass.getuser()
    fileslist = os.listdir(os.path.join(os.path.dirname(__file__), 'files'))
    for filename in fileslist:
        localname = os.path.join(os.path.dirname(__file__), 'files', filename)
        deployname = os.path.join('/home', username, '.' + filename)
        #print("[INFO] {0} -> {1}".format(localname, deployname))
        if not os.path.islink(deployname):
            print("[INFO] Could link {0}".format(deployname))
            #os.symlink("src_dir", "dst_dir")

link_files()


def main():
    """ Run any function as a parameter (fab-like). """
    pass

