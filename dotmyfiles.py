#!/usr/bin/python
# -*- coding: utf-8 -*-
""" dotfiles installation script.
    Created by Stéphane Péchard on 2012-07-23. """

# system
import argparse
import getpass
import os
import re
from subprocess import call


def print_info_ok(message):
    """ Format a string into an OK information shell line. """
    print('[INFO] \x1b[{0}m{1}\x1b[0m'.format(32, message))


def print_info_ko(message):
    """ Format a string into an KO information shell line. """
    print('[INFO] \x1b[{0}m{1}\x1b[0m'.format(33, message))


def current_dir():
    return os.path.dirname(os.path.abspath(__file__))


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
    """ Create symbolic links to everything in the files directory
        except already dotted files. """
    username = getpass.getuser()
    fileslist = os.listdir(os.path.join(os.path.dirname(__file__), 'files'))
    for filename in fileslist:
        if not filename.startswith('.'):
            localname = os.path.join(current_dir(), 'files', filename)
            deployname = os.path.join('/home', username, '.' + filename)
            make_symlink(localname, deployname)


def link_custom():
    """ Create specific symbolic links to customed files. """
    fileslist = os.listdir(os.path.join(os.path.dirname(__file__), 'custom'))
    for filename in fileslist:
        if not filename.startswith('.'):
            (root, ext) = os.path.splitext(filename) 
            if ext == '.zsh-theme':
                localname = os.path.join(current_dir(), 'custom', filename)
                deployname = os.path.join(current_dir(), 'files/oh-my-zsh/themes', filename)
                make_symlink(localname, deployname)


def run_install(args):
    """ Install every dotfile. """
    init()
    link_files()
    link_custom()


def run_status(args):
    """ Print information about the current state of the user's dotfiles. """
    pass


def main():
    """ Do everything. """
    parser = argparse.ArgumentParser()
    parser.add_argument('command', help="The command you want to use")
    args = parser.parse_args()
    
    # dispatch command to functions
    if args.command == 'install':
        run_install(args)

    if args.command == 'status':
        run_status(args)

    

if __name__ == '__main__':
    main()
