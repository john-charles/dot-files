#!/bin/sh

_BC_SCRIPT_ROOT=`dirname ${BASH_SOURCE[0]}`

source $_BC_SCRIPT_ROOT/functions/wk.sh
source $_BC_SCRIPT_ROOT/functions/pause.sh

export PATH=$HOME/System/bin:$PATH

source $_BC_SCRIPT_ROOT/etc/aliases.sh

source $_BC_SCRIPT_ROOT/etc/ps1.sh
export PS1=`cat $_BC_SCRIPT_ROOT/etc/ps1.txt`

_BC_SCRIPT_ROOT="" # Clean up after we run.
