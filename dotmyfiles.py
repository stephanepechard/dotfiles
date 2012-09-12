#!/usr/bin/python
# -*- coding: utf-8 -*-
""" dotfiles installation script.
    Created by Stéphane Péchard on 2012-07-23. """

# system
import argparse
import os
import re
from subprocess import call


def print_info_ok(message):
    """ Format a string into an OK information shell line. """
    print('[INFO] \x1b[{0}m{1}\x1b[0m'.format(32, message))


def print_info_ko(message):
    """ Format a string into an KO information shell line. """
    print('[INFO] \x1b[{0}m{1}\x1b[0m'.format(33, message))


def print_error(message):
    """ Format a string into an KO information shell line. """
    print('[ERROR] \x1b[{0}m{1}\x1b[0m'.format(31, message))


def current_dir():
    return os.path.dirname(os.path.abspath(__file__))


def init():
    """ Get all third-party code into git submodules. """
    try:
        call(['git', 'submodule', '--quiet', 'init'])
        call(['git', 'submodule', '--quiet', 'update'])
    except OSError:
        print_error("Install git to be able to init your submodules!\n")


def make_symlink(src, dst):
    """ Securely create a symbolic link. """
    if not os.path.islink(dst):
        if not os.path.exists(dst):
            print_info_ok("{0} -> {1}".format(src, dst))
            os.symlink(src, dst)
        else:
            print_info_ko("There is a file already named {0}".format(dst))
    else:
        print("[INFO] {0} is already linked to {1}"
                .format(os.path.basename(src), dst))


def link_files():
    """ Create symbolic links to everything in the files directory
        except already dotted files. """
    fileslist = os.listdir(os.path.join(os.path.dirname(__file__), 'files'))
    for filename in fileslist:
        if not filename.startswith('.'):
            localname = os.path.join(current_dir(), 'files', filename)
            deployname = os.path.join(os.environ['HOME'], '.' + filename)
            make_symlink(localname, deployname)


def show_links():
    """ Check symbolic links already installed against what's into 'files'."""
    fileslist = os.listdir(os.path.join(os.path.dirname(__file__), 'files'))

    max_length = 0
    dst_list = []
    for filename in fileslist:
        if not filename.startswith('.'):
            localname = os.path.join(current_dir(), 'files', filename)
            dst = os.path.join(os.environ['HOME'], '.' + filename)
            dst_list.append((localname, dst))
            if max_length < len(dst):
                max_length = len(dst)

    dst_list = sorted(dst_list, key=lambda d: d[0])   # sort by localname
    max_length = max_length + 4
    for localname, dst in dst_list:
        if not os.path.islink(dst):
            if not os.path.exists(dst):
                print_info_ok("{0:{1}} No link (yet)!".format(dst, max_length))
            else:
                print_info_ko("{0:{1}} There's a file at this place..."
                        .format(dst, max_length))
        else:
            target = os.path.join(os.path.dirname(dst), os.readlink(dst))
            if target == localname:
                print("[INFO] {0:{1}} OK".format(dst, max_length))
            else:
                print_info_ko("{0:{1}} There's a link to {2} at this place..."
                        .format(dst, max_length, target))

    print("\n[INFO] Link your files with: ./dotmyfiles.py install")


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
    show_links()


def main():
    """ Do everything. """
    parser = argparse.ArgumentParser(description="Link user configuration "
             "files (dot files) contained into the files directory.")
    parser.add_argument('command',
            help="The command you want to use. Possible commands are "
            "install (install every dotfile) "
            "status (print status of each dotfile)")
    args = parser.parse_args()
    
    # dispatch command to functions
    if args.command == 'install':
        run_install(args)

    if args.command == 'status':
        run_status(args)

    

if __name__ == '__main__':
    main()

