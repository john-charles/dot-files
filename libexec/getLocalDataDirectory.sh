function __getLocalDataDirectoryLinux (){
    # http://standards.freedesktop.org/basedir-spec/basedir-spec-latest.html
    if [ -z "$XDG_DATA_HOME" ]; then
        echo "$HOME/.local/share/$1"
    else
        echo "$XDG_DATA_HOME/$1"
    fi
}

function __getLocalDataDirectoryCygwin (){

    if [ ! -z "$LOCALAPPDATA" ]; then
        cygpath -u "$LOCALAPPDATA/$1"
    else
        cygpath -u "$APPDATA/$1"
    fi
}

function __getLocalDataDirectoryMinGW (){

    if [ ! -z "$LOCALAPPDATA" ]; then
        echo "$LOCALAPPDATA/$1" | sed 's/\\/\//g'
    else
        echo "$APPDATA/$1" | sed 's/\\/\//g'
    fi
}

osEnv=`uname -s`;

case $osEnv in
    
    Linux)
        __getLocalDataDirectoryLinux $1
        ;;

    MINGW*)
        __getLocalDataDirectoryMinGW $1
        ;;

    CYGWIN*)
        __getLocalDataDirectoryCygwin $1
        ;;
    
    *)
        echo "Unknown environment '$osEnv'" >&2
        exit 1
        ;;

esac
