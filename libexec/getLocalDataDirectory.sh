function __getLocalDataDirectoryLinux (){
    # http://standards.freedesktop.org/basedir-spec/basedir-spec-latest.html
    if [ -z "$XDG_DATA_HOME" ]; then
        echo "$HOME/.local/share/$1"
    else
        echo "$XDG_DATA_HOME/$1"
    fi
}



osEnv=`uname -s`;

case $osEnv in
    
    Linux)
        __getLocalDataDirectoryLinux $1
        ;;
    
    *)
        echo "Unknown environment '$osEnv'"
        return 1
        ;;

esac