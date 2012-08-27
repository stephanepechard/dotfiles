#!/usr/bin/python
# -*- coding: utf-8 -*-
""" dotfiles installation script.
    Created by Stéphane Péchard on 2012-07-23. """

# system
import getpass
import os
import re
from subprocess import call


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
            os.symlink(src, dst)
            print("[INFO] {0} -> {1}".format(src, dst))
        else:
            print("[INFO] There is a file already named {0}".format(dst))
    else:
        print("[INFO] {0} is aleady linked to {1}".format(src, dst))


def link_files():
    """ Create symbolic links to everything in the files directory. """
    username = getpass.getuser()
    fileslist = os.listdir(os.path.join(os.path.dirname(__file__), 'files'))
    for filename in fileslist:
        localname = os.path.join(os.path.dirname(__file__), 'files', filename)
        deployname = os.path.join('/home', username, '.' + filename)
        print("[INFO] {0} -> {1}".format(localname, deployname))

        if not os.path.islink(deployname):
            print("[INFO] Currently no link {0}".format(deployname))

            if os.path.exists(deployname):
                print("...... but the file exists!")

            os.symlink(localname, deployname)
        else:
            currentname = os.readlink(deployname)
            print("[INFO] Link currently points to: {0}".format(currentname))


def link_custom():
    fileslist = os.listdir(os.path.join(os.path.dirname(__file__), 'custom'))
    for filename in fileslist:
        (root, ext) = os.path.splitext(filename) 
        if ext == '.zsh-theme':
           os.symlink(filename, os.path.join('files/oh-my-zsh/themes', filename))



def main():
    """ Do everything. """
    init()
    link_files()
    link_custom()


if __name__ == '__main__':
    main()

