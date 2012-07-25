# git lib stuff
ZSH_THEME_GIT_PROMPT_PREFIX="[%{%B%F{blue}%}"
ZSH_THEME_GIT_PROMPT_SUFFIX="]"
ZSH_THEME_GIT_PROMPT_DIRTY="%{%F{red}%}*%{$reset_color%}"
ZSH_THEME_GIT_PROMPT_CLEAN=""

# left prompt
PROMPT='%{$fg[cyan]%}%T%{$fg[white]%} %{$fg[red]%}%n%{$fg[cyan]%}@%{$fg[white]%}%m %{$fg[green]%}%0~ %{$fg[cyan]%}$%{$reset_color%} '

# right prompt
RPROMPT='$(git_prompt_info)'

