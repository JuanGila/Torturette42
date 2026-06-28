#!/bin/bash
set -e
# =========================
# COLORS-VARIABLES CONFIGURATION
# =========================
WHITE='\033[0;37m' 
BLUE='\033[0;36m'
GREEN='\033[0;32m'
RED='\033[0;31m'
BWhite='\033[1;37m' 
NC='\033[0m'
# =========================
# PACKAGES CONFIGURATION
# =========================
packages_ubuntu=(
	gcc
	libbsd-dev
	libncurses-dev
	valgrind
	python3-pip
	git
)

packages_arch=(
	gcc
	clang
	postgresql
	libbsd
	ncurses
	valgrind
	python-pip
	git
)
# =========================
# FUNCTIONS
# =========================
setup_install_dir() { # OK
    cd # cd $(dirname $0)
    if [ -z "${INSTALL_DIR}" ]; then
        INSTALL_DIR=$HOME
        read -p "Install Directory (default: $INSTALL_DIR): " user_input
        INSTALL_DIR=${user_input:-$INSTALL_DIR}
    fi
    export INSTALL_DIR
}

install_kitty() { # OK
    if ! command -v kitty >/dev/null 2>&1; then
        echo -e "${BLUE}[torturette]${WHITE} Installing Kitty...${NC}"
        curl -L https://sw.kovidgoyal.net/kitty/installer.sh | sh /dev/stdin
    fi
    # Si falla la instalación de Kitty, se detiene el script(intentar cambiar la detencion del script por check=0 y usar la imagen con docker)
    if ! command -v kitty >/dev/null 2>&1; then
        echo -e "${RED}[torturette]${WHITE} Kitty installation failed.${NC}"
        exit 1
    fi
    # Exportamos la variable de entorno PATH.
    export PATH="$HOME/.local/kitty.app/bin:$PATH"
}

check_packages_ubuntu() { # OK
    for package in "${packages_ubuntu[@]}"; do
        if dpkg -s "$package" &>/dev/null; then
            echo "✔️ $package is installed."
        else
            echo "❌ $package is not installed."
            check=0
        fi
    done
}

check_packages_arch() { # OK
    for package in "${packages_arch[@]}"; do
        if pacman -Qi "$package" &>/dev/null; then
            echo "✔️ $package is installed."
        else
            echo "❌ $package is not installed."
            check=0
        fi
    done
}

detect_os_and_check_packages() { # OK
    if [ "$(uname)" = "Darwin" ]; then
        check=0
        return
    fi
    # Detectamos el sistema operativo
    case $(lsb_release -is) in
        "Ubuntu"|"Debian")
            check_packages_ubuntu
            ;;
        "Arch"|"EndeavourOS")
            check_packages_arch
            ;;
        *)
            check=0
            ;;
    esac
}

install_torturette() {
    echo -e "${GREEN} Installing torturette (source)...${NC}"
    git clone --recursive https://github.com/xicodomingues/torturette.git "$INSTALL_DIR/torturette"
    cd "$INSTALL_DIR/torturette"
    pip install -r requirements.txt
}

install_torturette_image() {
    # Eliminamos posibles archivos/residuos temporales de la imagen.
    rm -rf $INSTALL_DIR/.tmp_torturette # rm -drf
    echo -e "${GREEN} Installing torturette-image...${NC}"
	echo -e "${GREEN} Installation of the torturette-image in progress${RESET}"
    # Si existe la carpeta de la instalacion normal, la eliminamos.
    if ls -l $INSTALL_DIR | grep "torturette" &> /dev/null; then
		rm -rf $INSTALL_DIR/torturette # rm -drf
		echo -e "${BLUE}torturette${GREEB} Uninstalled OK${RESET}"
    fi
    # Si no tenemos la imagen de torturette, la descargamos.
    if ! ls "$INSTALL_DIR" | grep "torturette-image" &>/dev/null; then # if ! ls -l "$INSTALL_DIR" | grep "torturette-image" &> /dev/null;
        git clone https://github.com/JuanGilabert/Torturette.git "$INSTALL_DIR/torturette-image"
    fi
    chmod +x "$INSTALL_DIR/torturette-image/run.sh"
    # Si no tenemos la imagen de torturette, usamos docker.
    if ! ls -l $INSTALL_DIR/torturette-image | grep "torturette.tar" &> /dev/null; then
		docker build -t torturette-image $INSTALL_DIR/torturette-image
		docker image save torturette-image > $INSTALL_DIR/torturette-image/torturette.tar
	fi
    # Si tenemos la imagen de torturette, la cargamos.
	if ls -l $INSTALL_DIR/torturette-image | grep "torturette.tar" &> /dev/null; then
		docker load < $INSTALL_DIR/torturette-image/torturette.tar
	fi
	source $INSTALL_DIR/torturette-image/utils/install_zshrc.sh
}

final_message() { # OK
    echo -e "${BLUE}[torturette]${GREEN} Installation completed!${NC}"
    echo -e "${WHITE}Use hades or torturette commands.${NC}"
}
# =========================
# TORTURRETTE MAIN SCRIPT
# =========================
check=1

setup_install_dir
install_kitty
detect_os_and_check_packages

if [ "$check" -eq 1 ]; then
    echo "Everything OK → torturette install"
    install_torturette
else
    echo "Missing packages → torturette-image install"
    install_torturette_image
fi

final_message
exec "$SHELL"