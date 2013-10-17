[![Bitdeli Badge](https://d2weczhvl823v0.cloudfront.net/stephanepechard/dotfiles/trend.png)](https://bitdeli.com/free "Bitdeli Badge")

dotfiles
========
You probably don't care about my very own dotfiles. What could be
of any interest to you is a little script to install all these dotfiles
on any UNIX-like device. I called it `dotmyfiles.py`.


Typical usage
-------------
Put all your files to be dotted into the `files` directory, **WITHOUT** the dot.
Edit the `custom.py` file to specify the link to be done by the script between
a file into the `custom` directory and its target which can be anywhere in
your filesystem. When it's ready, type:

    ./dotmyfiles install

to create links between your files into the `files` directory and their
dotted counterparts. As everything here is linked, you should never remove
what's in the `files` directory. This is **NOT** a copy.

Don't worry what is already into your home, nothing is ever overwritten.
The command will indicate to you the current status of the install.
To be sure of what you do before, you can use:

    ./dotmyfiles status

to print the status of each dotfile.

The simple:

    ./dotmyfiles update

will fetch any submodule you installed into your repository (I do that, look
at my `.gitmodules` file, I install Vim plugins as git submodules.)


Command-t
---------
The [command-t](https://github.com/wincent/Command-T) extension requires
Vim with ruby support, and furthermore, the ruby code depends
on a C extension for extra speed. There's a specific command to do it directly:

    ./dotmyfiles make_commandT

Neat, right?
