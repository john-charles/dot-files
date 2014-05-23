#!/bin/bash

source utils/pause.sh

INSTALL_DIR=$(./utils/findLocals.sh bashCustom)

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

while true; do

    echo "Do you want to source bash customizations in your .bashrc?"
    echo "If this is the first time your running this script you most"
    read -p "likely want to answer yes! (y/n)?" yn

    case $yn in
        [Yy]*)
            echo "Appending 'source $INSTALL_DIR/main.sh' to ~/.bashrc"
            echo "source $INSTALL_DIR/main.sh" >> ~/.bashrc
            break;;
        [Nn]*)
            echo "Not appending 'source $INSTALL_DIR/main.sh' to ~/.bashrc"
            break;;
        * )
            echo "Please enter (y/n) only!"
    esac

done

while true; do

    read -p "Source the newly installed customizations now? (y/n)" yn

    case $yn in
        [Yy]*)
            echo "Sourcing $INSTALL_DIR/main.sh now!"
            source $INSTALL_DIR/main.sh
            break;;
        [Nn]*)
            echo "Not Sourcing $INSTALL_DIR/main.sh"
            break;;
        *)
            echo "Please enter (y/n)"
    esac

done

pause "All Done, press [ENTER] to exit!"


