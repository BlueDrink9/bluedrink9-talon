language: en
app: vscode
app: codium
-
# tag(): user.vim_send
# tag(): user.panes

settings():
    # Reduce flakiness when multiple keys being pressed.
    # insert_wait = 10
    # hotkey_wait = 10
    # key_wait = 10


bar variables:
    user.run_rpc_command("workbench.debug.action.focusVariablesView")
    key(down)
termy: user.vscode_and_wait("workbench.action.terminal.toggleTerminal")
complete: key(ctrl-e)
run last:
    edit.save()
    # Up + enter
    user.terminal_send("\u001b[A\u000d")

command previous:
    user.run_rpc_command("workbench.action.terminal.scrollToPreviousCommand")
command next:
    user.run_rpc_command("workbench.action.terminal.scrollToNextCommand")

complete: key(ctrl-e)
completion <user.number_key>:
    key("tab:{number_key}")
    key(ctrl-e)

# Find session
scout (sesh | recent) [<user.prose>]$:
    user.dialogue_search_or_enter("workbench.action.openRecent", prose or "")
pop sesh [<user.prose>]$:
    user.dialogue_search_or_enter("workbench.action.openRecent", prose or "")
    sleep(150ms)
    key(enter)

pop (file | files | filed) [<user.filename>]$:
    user.dialogue_search_or_enter("workbench.action.quickOpen", filename or "", true)
    sleep(400ms)
    key(enter)

pop symbol [<user.prose>]$:
    user.dialogue_search_or_enter("workbench.action.gotoSymbol", prose or "", true)
    sleep(200ms)
    key(enter)

# Find a symbol
scout symbol [<user.prose>]$:
    user.run_rpc_command("workbench.action.showAllSymbols")
    sleep(50ms)
    user.insert_formatted(prose or "", "CAMEL_CASE")

pop sibling:
    user.find_sibling_file()
    sleep(200ms)
    key(enter)

debug expand:
    user.run_rpc_command("workbench.debug.action.toggleRepl")
    key(shift-tab)
    key(end)
    key(enter)

window reload: user.run_rpc_command("workbench.action.reloadWindow")
scout again: user.run_rpc_command("rerunSearchEditorSearch")

# Navigation
go line <number>: edit.jump_line(number - 1)
pop back: user.run_rpc_command("workbench.action.openPreviousRecentlyUsedEditor")
pop forward: user.run_rpc_command("workbench.action.openNextRecentlyUsedEditor")
focus editor: user.run_rpc_command("workbench.action.focusActiveEditorGroup")

# swap to other split
cross: user.run_rpc_command("workbench.action.focusNextGroup")
split up: user.run_rpc_command("workbench.action.moveEditorToAboveGroup")
split down: user.run_rpc_command("workbench.action.moveEditorToBelowGroup")
split left: user.run_rpc_command("workbench.action.moveEditorToLeftGroup")
split right: user.run_rpc_command("workbench.action.moveEditorToRightGroup")
focus up: user.run_rpc_command("workbench.action.focusAboveGroup")
focus down: user.run_rpc_command("workbench.action.focusBelowGroup")
focus left: user.run_rpc_command("workbench.action.focusLeftGroup")
focus right: user.run_rpc_command("workbench.action.focusRightGroup")
shrink width: user.run_rpc_command("workbench.action.decreaseViewWidth")
shrink height: user.run_rpc_command("workbench.action.decreaseViewHeight")
expand width: user.run_rpc_command("workbench.action.increaseViewWidth")
expand height: user.run_rpc_command("workbench.action.increaseViewHeight")
split flip: user.run_rpc_command("workbench.action.toggleEditorGroupLayout")
split clear: user.run_rpc_command("workbench.action.joinTwoGroups")
split solo: user.run_rpc_command("workbench.action.editorLayoutSingle")
maximize: user.run_rpc_command("workbench.action.toggleEditorWidths")
