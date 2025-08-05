mode: command
mode: user.cursorless_spoken_form_test
tag: user.cursorless
-

# Override the cursorless change, drink and pour commands to also enter insert mode.
change <user.cursorless_target>:
    user.cursorless_command("clearAndSetSelection", cursorless_target)
    user.run_rpc_command("vscode-neovim.lua", "vim.cmd('startinsert')")
drink <user.cursorless_target>:
    user.cursorless_command("editNewLineBefore", cursorless_target)
    user.run_rpc_command("vscode-neovim.lua", "vim.cmd('startinsert')")
pour <user.cursorless_target>:
    user.cursorless_command("editNewLineAfter", cursorless_target)
    user.run_rpc_command("vscode-neovim.lua", "vim.cmd('startinsert')")

(insert <user.cursorless_destination> | <user.cursorless_destination> insert) <user.keys>$:
    user.cursorless_insert(cursorless_destination, keys)

# Allow formatting targets
format <user.formatters> <user.cursorless_target>:
    user.cursorless_reformat(cursorless_target, formatters)

# Set a breakpoint at this target
break point <user.cursorless_target>:
    user.cursorless_ide_command("editor.debug.action.toggleBreakpoint", cursorless_target)

# Evaluate in debug console
bug run <user.cursorless_target> | buggy <user.cursorless_target>:
    user.cursorless_ide_command("editor.debug.action.selectionToRepl", cursorless_target)

# Evaluate in terminal
code run <user.cursorless_target> | code it <user.cursorless_target>:
    command = user.get_repl_runner()
    user.cursorless_ide_command(command, cursorless_target)

# Make a comment before the target line
make comment <user.cursorless_target>:
    user.cursorless_command("editNewLineBefore", cursorless_target)
    user.run_rpc_command("vscode-neovim.lua", "vim.cmd('startinsert')")
    user.run_rpc_command("editor.action.commentLine")
