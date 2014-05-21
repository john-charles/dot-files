#!/bin/sh

source utils/pause.sh

INSTALL_DIR="$HOME/Desktop/.bashCustomizations"

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
    copyDirectory projectsDir

}



echo "Setting up bash customizations!"

prepTarget
copyFiles


pause "Press [ENTER] to continue!"


