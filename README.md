Documentation

http://stevelosh.com/blog/2010/02/my-extravagant-zsh-prompt/
http://www.drbunsen.org/text-triumvirate.html



Installation

    git clone git://github.com/nelstrom/dotfiles.git

Where possible, Vim plugins are installed as git submodules. Check these out by
running the commands:

    cd dotfiles
    git submodule init
    git submodule update


### Command-t

The command-t extension require Vim with ruby support, and furthermore, the
ruby code depends on a C extension for extra speed. The usual pathogen
installation proceedure didn't work for me, but I followed these steps to make
it work:

    cd ~/dotfiles/vim/bundle/command-t/ruby/command-t
    ruby extconf.rb
    make

That did the trick.

