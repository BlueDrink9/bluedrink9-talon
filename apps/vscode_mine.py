from talon import Context, Module, actions
mod = Module()

ctx = Context()
ctx.matches = "app: vscode"


linux_ctx = Context()
linux_ctx.matches = r"""
os: linux
app: vscode
language: en
"""

@linux_ctx.action_class("user")
class LinuxUserActions:
    def trigger_command_server_command_execution():
        # Work around bug with upper f-keys in VSCode on Linux. See
        # https://github.com/pokey/command-server/issues/9#issuecomment-963733930
        actions.key("ctrl-shift-alt-super-`")

@mod.action_class
class Actions:
    def terminal_send(sequence: str):
        """Send a sequence to the vscode terminal, bypassing vscode shortcut handling etc."""
        # Send ctrl f, mapped to fzf command
        actions.user.run_rpc_command("workbench.action.terminal.sendSequence", {"text": sequence})

    def get_repl_runner() -> str:
        """Get the VSCode command required to run code for the current language"""
        lang = actions.code.language()
        try:
            command = {
                "r": "r.runSelection",
                # Could also use jupyter for this I guess
                "python": "python.execSelectionInTerminal",
            }[lang]
            return command
        except KeyError:
            actions.app.notify(f"Language '{lang}' does not have a defined run command yet in vscode_mine.py")

    def dialogue_search_or_enter(
        rpc_command: str, text: str = None, skip_first_if_empty: bool = False
    ):
        """Open the quick open dialog in VSCode, optionally inserting text"""
        actions.user.run_rpc_command(rpc_command)
        if text:
            actions.sleep("50ms")
            actions.insert(text)
        elif skip_first_if_empty:
            # Down to first file that isn't the current one
            actions.key("down")
