code.language: r
app: vscode
app: codium
-

debug collect:
    user.run_rpc_command("workbench.debug.action.focusRepl")
    key(up)
    user.edit_command("goAfter", "fileEnd")
    insert(" %>% collect()")
    key(enter)
