#!/bin/bash

source functions/pause.sh

INSTALL_DIR=$HOME/System


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

setupSource

pause "All Done, press [ENTER] to exit!"


