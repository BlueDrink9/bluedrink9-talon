app: neovim
and not tag: user.vim_mode_command
-
file local edit [<user.text>]:     user.vim_run_command_exterm(":le ")
user.insert(user.text or "")
