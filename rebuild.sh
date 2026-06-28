#!/bin/bash
WHITE='\033[0;37m' 
BLUE='\033[0;36m'
GREEN='\033[0;32m'
RED='\033[0;31m'
NC='\033[0m'
if ls -l $HOME | grep "torturette-image" &> /dev/null; then
    source $HOME/torturette-image/utils/remove_docker.sh
	rm -f $HOME/torturette-image/torturette.tar
    source $HOME/torturette-image/install.sh
    echo -e "${BLUE}[torturette] ${WHITE}Rebuilded ${GREEN}OK"
fi
