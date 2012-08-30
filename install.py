#!/usr/bin/python
# -*- coding: utf-8 -*-
""" dotfiles installation script.
    Created by Stéphane Péchard on 2012-07-23. """

# system
import getpass
import os
import re
from subprocess import call

# globals
THISDIR = os.path.dirname(os.path.abspath(__file__))


def print_info_ok(message):
    """ Format a string into an OK information shell line. """
    print('[INFO] \x1b[{0}m{1}\x1b[0m'.format(32, message))


def print_info_ko(message):
    """ Format a string into an KO information shell line. """
    print('[INFO] \x1b[{0}m{1}\x1b[0m'.format(33, message))


def init():
    """ Get all third-party code. """
    call(['git', 'submodule', 'init'])
    call(['git', 'submodule', 'update'])

#    call(['git', 'clone',
#    'git://github.com/altercation/solarized.git',
#    'external/solarized'])
#    call(['git', 'clone',
#    'git://github.com/phiggins/konsole-colors-solarized.git',
#    'external/konsole-colors-solarized'])
#    call(['git', 'clone',
#    'git://github.com/hayalci/kde-colors-solarized.git',
#    'external/kde-colors-solarized'])


def make_symlink(src, dst):
    """ Securely create a symbolic link. """
    if not os.path.islink(dst):
        if not os.path.exists(dst):
            print_info_ok("{0} -> {1}".format(src, dst))
            os.symlink(src, dst)
        else:
            print_info_ko("There is a file already named {0}".format(dst))
    else:
        print_info_ko("{0} is aleady linked to {1}".format(src, dst))


def link_files():
    """ Create symbolic links to everything in the files directory. """
    username = getpass.getuser()
    fileslist = os.listdir(os.path.join(os.path.dirname(__file__), 'files'))
    for filename in fileslist:
        localname = os.path.join(THISDIR, 'files', filename)
        deployname = os.path.join('/home', username, '.' + filename)
        make_symlink(localname, deployname)


def link_custom():
    """ Create specific symbolic links to customed files. """
    fileslist = os.listdir(os.path.join(os.path.dirname(__file__), 'custom'))
    for filename in fileslist:
        (root, ext) = os.path.splitext(filename) 
        if ext == '.zsh-theme':
            localname = os.path.join(THISDIR, 'custom', filename)
            deployname = os.path.join(THISDIR, 'files/oh-my-zsh/themes', filename)
            make_symlink(localname, deployname)


def main():
    """ Do everything. """
    init()
    link_files()
    link_custom()


if __name__ == '__main__':
    main()

