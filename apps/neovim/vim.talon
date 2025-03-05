app: neovim
and not tag: user.vim_mode_command
-
# tag(): user.panes
# tag(): user.vim_send

file local edit [<user.text>]:
    user.vim_run_command_exterm(";le ")
    insert(user.text or "")
