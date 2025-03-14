language: en
app: vscode
app: codium
-
# tag(): user.vim_send
# tag(): user.panes

# TODO: make lang-specific
# send <user.cursorless_target>: user.cursorless_ide_command("r.runSelection", cursorless_target)
bar variables: user.run_rpc_command("workbench.debug.action.focusVariablesView")
complete: key(ctrl-e)
