function wk(){
    cd ~/Projects/$1
}

function _wk_complete(){

    local cur=${COMP_WORDS[COMP_CWORD]}
    COMPREPLY=( $(compgen -W "`ls --color=no -a ~/Projects`" -- $cur) )
}

complete -F _wk_complete wk
