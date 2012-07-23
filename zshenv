# /etc/zsh/zshenv ou ~/.zshenv
# Fichier de configuration de zsh
# Formation Debian GNU/Linux par Alexis de Lattre
# http://formation-debian.via.ecp.fr/

# Le PATH = répertoires dans lequels le shell va chercher les commandes
# ATTENTION : le répertoire courant ne fait pas partie du PATH
export PATH="/usr/local/bin:/usr/local/sbin:/bin:/usr/bin:/usr/sbin:/usr/games:/sbin:$HOME/bin:$HOME/.local/bin"

# Viewer/Editeur par defaut (pour Crontab, CVS,...)
#export VISUAL=vim
#export EDITOR=vim

# Permissions rw-r--r-- pour les fichiers crées
# et rwxr-xr-x pour les répertoires crées
umask 022

export DROPBOXDIR="/home/stephane/data/Dropbox"
