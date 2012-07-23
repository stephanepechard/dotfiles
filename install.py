#!/usr/bin/python
-*- coding: utf-8 -*-
""" dotfiles installation script.
    Created by Stéphane Péchard on 2012-07-23. """

# system
import subprocess

def clone_omz():
    subprocess.call(['git', 'clone',
        'git://github.com/robbyrussell/oh-my-zsh.git', 'files/oh-my-zsh'])

def clone_solarized():
    subprocess.call(['git', 'clone',
        'git://github.com/altercation/solarized.git', 'solarized']













