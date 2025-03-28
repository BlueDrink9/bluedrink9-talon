
mode: command
mode: user.cursorless_spoken_form_test
tag: user.cursorless
-

# Override the cursorless change command to also enter insert mode.
change <user.cursorless_target>:
    user.cursorless_command("clearAndSetSelection", cursorless_target)
    user.run_rpc_command("vscode-neovim.lua", "vim.cmd('startinsert')")

# Allow formatting targets
<user.formatters> <user.cursorless_target>:
    user.cursorless_reformat(cursorless_target, formatters)

# Set a breakpoint at this target
break point <user.cursorless_target>:
    user.cursorless_ide_command("editor.debug.action.toggleBreakpoint", cursorless_target)

# Evaluate in debug console
bug run <user.cursorless_target>:
    user.cursorless_ide_command("editor.debug.action.selectionToRepl", cursorless_target)

# TODO: gate by language.
code run <user.cursorless_target>:
    user.cursorless_ide_command("r.runSelection", cursorless_target)
