#!/bin/sh

_BC_SCRIPT_ROOT=`dirname ${BASH_SOURCE[0]}`

source $_BC_SCRIPT_ROOT/functions/wk.sh
source $_BC_SCRIPT_ROOT/functions/pause.sh

export PATH=$HOME/System/bin:$PATH

_BC_SCRIPT_ROOT="" # Clean up after we run.
