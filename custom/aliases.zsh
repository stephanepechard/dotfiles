# the way i like ls
alias ls='ls --color=auto --classify --tabsize=0 --literal -G --show-control-chars --human-readable'
alias ll='ls -l'
alias la='ls -a'
alias lla='ls -la'
# color and number of line in 'grep'
alias grep='grep -n --color=auto'
alias ggrep='git grep --color -n -P';
# careful with that axe, eugene
alias cp='cp --interactive'
alias mv='mv --interactive'
alias rm='rm --interactive'
# useful stuff
alias c='clear'
alias less='less --quiet'
alias s='cd ..'
alias df='df --human-readable'
alias du='du --human-readable'
alias md='mkdir'
alias rd='rmdir'
alias upgrade='sudo aptitude update && sudo aptitude safe-upgrade && sudo aptitude autoclean'
alias kate='kate -u'
alias f='find . -name'
alias pylint='pylint --rcfile=~/.pylintrc'
alias a='source venv/bin/activate'
alias r='python manage.py runserver'
alias josm='java -jar -Xmx1524M ~/bin/josm-tested.jar'
# anti-clumsy fingers
alias sl=ls # often screw this up
alias kk='ll'
alias mm='ll'
