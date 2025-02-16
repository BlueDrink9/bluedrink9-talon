
from talon import Context, Module, actions
mod = Module()
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
