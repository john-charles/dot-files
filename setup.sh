#!/bin/bash

source utils/pause.sh

PATH=./libexec:$PATH

INSTALL_DIR=$(getLocalDataDirectory.sh bashCustom)

function prepTarget(){
    echo "Preparing installation directroy: $INSTALL_DIR"
    rm -rf $INSTALL_DIR
    mkdir -p $INSTALL_DIR
}

function copyDirectory(){

    mkdir -p $INSTALL_DIR/$1
    cp -r ./$1/* $INSTALL_DIR/$1/
}



function copyFiles(){

    cp ./main.sh $INSTALL_DIR/main.sh
    copyDirectory utils
    copyDirectory libexec
    copyDirectory dirUtils

}

function setupSource(){
    
    SOURCE_LINE="source $INSTALL_DIR/main.sh"
    
    if grep -Fxq "$SOURCE_LINE" "$HOME/.bashrc"; then
        echo "dot files custom already installed in bashrc."
    else
        echo "Appending 'source $INSTALL_DIR/main.sh' to ~/.bashrc"
        echo "source $INSTALL_DIR/main.sh" >> ~/.bashrc
        echo "Please run source ~/.bashrc to activate..."
    fi
    
}



echo "Setting up bash customizations!"

prepTarget
copyFiles
setupSource


pause "All Done, press [ENTER] to exit!"


