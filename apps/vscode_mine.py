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
