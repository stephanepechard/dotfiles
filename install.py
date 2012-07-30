#!/usr/bin/python
# -*- coding: utf-8 -*-
""" dotfiles installation script.
    Created by Stéphane Péchard on 2012-07-23. """

# system
import getpass
import os
import re
from subprocess import call


def install():
    """ Do everything. """
    clone_code()
    link_files()
    link_config()


def clone_code():
    """ Get all third-party code. """
    call(['git', 'clone',
    'git://github.com/robbyrussell/oh-my-zsh.git',
    'files/oh-my-zsh'])
    call(['git', 'clone',
    'git://github.com/altercation/solarized.git',
    'external/solarized'])
    call(['git', 'clone',
    'git://github.com/phiggins/konsole-colors-solarized.git',
    'external/konsole-colors-solarized'])
    call(['git', 'clone',
    'git://github.com/hayalci/kde-colors-solarized.git',
    'external/kde-colors-solarized'])


def link_files():
    """ Create symbolic links to everything in the files directory. """
    username = getpass.getuser()
    fileslist = os.listdir(os.path.join(os.path.dirname(__file__), 'files'))
    for filename in fileslist:
        localname = os.path.join(os.path.dirname(__file__), 'files', filename)
        deployname = os.path.join('/home', username, '.' + filename)
        #print("[INFO] {0} -> {1}".format(localname, deployname))

        if not os.path.islink(deployname):
            print("[INFO] Currently no link {0}".format(deployname))

            if os.path.exists(deployname):
                print("...... but the file exists!")

            #os.symlink("src_dir", "dst_dir")
        else:
            currentname = os.readlink(deployname)
            print("[INFO] Link currently points to: {0}".format(currentname))


def link_custom():
    fileslist = os.listdir(os.path.join(os.path.dirname(__file__), 'custom'))
    for filename in fileslist:
    #    if ext == 'zsh':
    #       os.symlink( 
        print(filename)

link_custom()


def main():
    """ Run any function as a parameter (fab-like). """
    class_functions = []
    with open(__file__, 'r') as f:
        for line in f:
            matches = re.match(r"def (.*)():", line)
            if (matches):
                print(matches.groups()[0])


if __name__ == '__main__':
    main()

