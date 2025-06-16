from talon import Module, Context, actions, app
import subprocess
from pathlib import Path

mod = Module()
mod.tag("send", desc="Tag for apps that use vim motions to send lines to repl")


ctx_fm = Context()
ctx_fm.matches = r"""
tag: user.file_manager
"""

@mod.action_class
class UserActions:
    def peek_file(f: str):
        """Open each folder in the inputted path and then open the final file, then
        ascend back to the original directory. Useful when you work with multiple
        folders that contain similar structure - always stay in the top level, then
        map utterances to open some of the commonly accessed files for that
        particular top level folder. """


@ctx_fm.action_class("user")
class UserActions:
    def peek_file(f: str):
        """Open each folder in the inputted path and then open the final file, then
        ascend back to the original directory. Useful when you work with multiple
        folders that contain similar structure - always stay in the top level, then
        map utterances to open some of the commonly accessed files for that
        particular top level folder. """
        parts = Path(f).parts

        # Define own function because Define and function becausefile_manager_open_directory does not work with relative directories
        def enter_entry(e):
            actions.insert(e)
            actions.key("enter")
            actions.sleep("100ms")

        for d in parts[:-1]:
            enter_entry(d)
        enter_entry(parts[-1])
        for _ in parts[:-1]:
            actions.user.file_manager_open_parent()
