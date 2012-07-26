# the way i like ls
alias ls='ls --classify --tabsize=0 --literal -G --show-control-chars --human-readable'
alias ll='ls -l'
alias la='ls -a'
alias lla='ls -la'
# color and number of line in 'grep'
alias grep='grep -n --color=auto'
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
alias upgrade='sudo aptitude update && sudo aptitude safe-upgrade && sudo aptitude autoclean && sudo update-flashplugin-nonfree --install'

# Push and pop directories on directory stack
alias pu='pushd'
alias po='popd'

# Basic directory operations
alias ...='cd ../..'
alias -- -='cd -'

# Super user
alias _='sudo'

# Show history
alias history='fc -l 1'

# List direcory contents
alias lsa='ls -lah'
alias l='ls -la'
alias ll='ls -l'
alias sl=ls # often screw this up

alias afind='ack-grep -il'

