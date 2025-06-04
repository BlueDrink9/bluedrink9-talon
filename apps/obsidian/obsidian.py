from talon import Context, Module, actions
from urllib.parse import quote
from webbrowser import open as open_uri


ADVANCED_URI_ENABLED = True

ctx = Context()
ctx.matches = r"""
app: Obsidian
"""

mod = Module()
mod.apps.obsidian = """
app: Obsidian
"""


def command_uri_or_client_fallback(command: str):
    """If advanced-uri is supported, use it to invoke the command.
    Otherwise, fall back to the client"""
    if ADVANCED_URI_ENABLED:
        uri = f"obsidian://advanced-uri?commandname={quote(command)}"
        open_uri(uri)
    else:
        actions.key('ctrl-p')
        actions.insert(command)
        actions.key('enter')


@mod.action_class
class Actions:
    def obsidian(command: str):
        """Invoke an action, by the name shown
        in the Obsidian command pallete"""
        command_uri_or_client_fallback(command)


@ctx.action_class("app")
class AppActions:
    # talon app actions
    def tab_open():
        actions.user.obsidian("New tab")

    def tab_close():
        actions.user.obsidian('Close current tab')

    def tab_next():
        actions.user.obsidian('Go to next tab')

    def tab_previous():
        actions.user.obsidian('Go to previous tab')

    def tab_reopen():
        actions.user.obsidian('Undo close tab')

    def window_close():
        actions.user.obsidian('Close window')


@ctx.action_class("user")
class UserActions:
    def tab_jump(number: int):
        actions.user.obsidian(f'Go to tab #{number}')

    def tab_final():
        actions.user.obsidian('Go to last tab')
