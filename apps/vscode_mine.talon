language: en
app: vscode
app: codium
-
# tag(): user.vim_send
# tag(): user.panes

bar variables:
    user.run_rpc_command("workbench.debug.action.focusVariablesView")
    key(down)
termy: user.vscode_and_wait("workbench.action.terminal.toggleTerminal")
complete: key(ctrl-e)
run last:
    edit.save()
    # Up + enter
    user.terminal_send("\u001b[A\u000d")

settings():
    # Reduce flakiness when multiple keys being pressed.
    insert_wait = 20
    hotkey_wait = 10
    key_wait = 20
