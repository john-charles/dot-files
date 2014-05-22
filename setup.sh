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
    copyDirectory dirUtils

}



echo "Setting up bash customizations!"

prepTarget
copyFiles

echo "source $INSTALL_DIR/main.sh" >> ~/.bashrc

pause "Press [ENTER] to continue!"


