#!/usr/bin/env zsh

# git lib stuff
ZSH_THEME_GIT_PROMPT_PREFIX="[%{%B%F{blue}%}"
ZSH_THEME_GIT_PROMPT_SUFFIX="]"
ZSH_THEME_GIT_PROMPT_DIRTY="%{%F{red}%}✘%{$reset_color%}"
ZSH_THEME_GIT_PROMPT_CLEAN="%{%F{green}%}✔%{$reset_color%}"
ZSH_THEME_GIT_PROMPT_ADDED="%{$FG[082]%}✚%{$reset_color%}"
ZSH_THEME_GIT_PROMPT_MODIFIED="%{$FG[166]%}✹%{$reset_color%}"
ZSH_THEME_GIT_PROMPT_DELETED="%{$FG[160]%}✖%{$reset_color%}"
ZSH_THEME_GIT_PROMPT_RENAMED="%{$FG[220]%}➜%{$reset_color%}"
ZSH_THEME_GIT_PROMPT_UNMERGED="%{$FG[082]%}═%{$reset_color%}"
ZSH_THEME_GIT_PROMPT_UNTRACKED="%{$FG[190]%}✭%{$reset_color%}"

# left prompt
PROMPT='%{$fg[cyan]%}%T%{$fg[white]%} %{$fg_bold[red]%}%n%{$fg_bold[cyan]%}@%{$fg_bold[white]%}%m %{$fg[green]%}%0~ %{$fg[cyan]%}$%{$reset_color%} '

# right prompt
RPROMPT='$(git_prompt_info)'
