language: en
app: vscode
app: codium
-
# tag(): user.vim_send
# tag(): user.panes

# TODO: make lang-specific
# send <user.cursorless_target>: user.cursorless_ide_command("r.runSelection", cursorless_target)
bar variables:
    user.run_rpc_command("workbench.debug.action.focusVariablesView")
    key(down)
termy: user.vscode_and_wait("workbench.action.terminal.toggleTerminal")
complete: key(ctrl-e)
run last:
    edit.save()
    # Up + enter
    user.terminal_send("\u001b[A\u000d")
