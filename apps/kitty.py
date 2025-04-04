import os
import re

from talon import Context, Module, actions, ui

ctx = Context()
mod = Module()

# TODO: find and add OSX matcher
mod.apps.kitty = r"""
os: linux
and app.name: kitty
"""

ctx.matches = r"""
app: kitty
"""

user_path = os.path.expanduser("~")
directories_to_remap = {}
directories_to_exclude = {}


# @ctx.action_class("app")
# class AppActions:
#     def tab_close():
#         actions.key("ctrl-shift-w")
#
#     def tab_open():
#         actions.key("ctrl-shift-t")


@ctx.action_class("edit")
class EditActions:
    def paste():
        actions.key("ctrl-shift-v")

    def copy():
        actions.key("ctrl-shift-c")

    # def find(text: str = None):
    #     actions.key("ctrl-shift-f")
    #     if text:
    #         actions.insert(text)


@ctx.action_class("user")
class UserActions:
    pattern = re.compile(r'\[([^\[\]]+)\](?=[^\[\]]*$)')
    def file_manager_current_path():
        path = ui.active_window().title

        match = UserActions.pattern.search(path)

        if match:
            path = match.group(1)
        else:
            return ""

        if path in directories_to_remap:
            path = directories_to_remap[path]

        if path in directories_to_exclude:
            path = ""
        return path

    # def file_manager_terminal_here():
    #     actions.key("ctrl-l")
    #     actions.insert("cmd.exe")
    #     actions.key("enter")

    # def file_manager_show_properties():
    #     """Shows the properties for the file"""
    #     actions.key("alt-enter")

    def file_manager_open_directory(path: str):
        """opens the directory that's already visible in the view"""
        actions.insert(f'cd "{path}"')
        actions.key("enter")
        actions.user.file_manager_refresh_title()

    def file_manager_select_directory(path: str):
        """selects the directory"""
        actions.insert(f'"{path}"')

    def file_manager_new_folder(name: str):
        """Creates a new folder in a gui filemanager or inserts the command to do so for terminals"""
        actions.insert(f'mkdir "{name}"')

    def file_manager_open_file(path: str):
        """opens the file"""
        actions.insert(path)
        # actions.key("enter")

    def file_manager_select_file(path: str):
        """selects the file"""
        actions.insert(path)

    def file_manager_open_volume(volume: str):
        """file_manager_open_volume"""
        actions.user.file_manager_open_directory(volume)
        actions.user.file_manager_refresh_title()

    def tab_jump(number: int):
        actions.key(f"ctrl-alt-{number}")

    # user.splits implementation:

    def split_window_right():
        """Move active tab to right split"""
        # TODO: decide whether this notification is good style
        actions.app.notify(
            '"Split right" is not possible in windows terminal without special configuration. Use "split vertically" instead.'
        )

    def split_window_left():
        """Move active tab to left split"""
        # TODO: decide whether this notification is good style
        actions.app.notify(
            '"Split left" is not possible in windows terminal without special configuration. Use "split vertically" instead.'
        )

    def split_window_down():
        """Move active tab to lower split"""
        # TODO: decide whether this notification is good style
        actions.app.notify(
            '"Split down" is not possible in windows terminal without special configuration. Use "split horizontally" instead.'
        )

    def split_window_up():
        """Move active tab to upper split"""
        # TODO: decide whether this notification is good style
        actions.app.notify(
            '"Split up" is not possible in windows terminal without special configuration. Use "split horizontally" instead.'
        )

    def split_window_vertically():
        """Splits window vertically"""
        actions.key("shift-alt-plus")

    def split_window_horizontally():
        """Splits window horizontally"""
        actions.key("shift-alt-minus")

    def split_flip():
        """Flips the orietation of the active split"""
        # TODO: decide whether this notification is good style
        actions.app.notify(
            '"Split flip" is not possible in windows terminal in default configuration.'
        )

    def split_window():
        """Splits the window"""
        # in this implementation an alias for split vertically
        actions.key("shift-alt-plus")

    def split_clear():
        """Clears the current split"""
        # also closes tab, because shortcut is the same
        # and closing a split does mean something differnent that in a code editor like vs code
        actions.key("ctrl-shift-w")

    def split_clear_all():
        """Clears all splits"""
        # TODO: decide whether to implement it at all since it either doesn't makes sense or closes the window/whole tab

    def split_next():
        """Goes to next split"""
        # TODO: decide whether this notification is good style
        actions.app.notify(
            '"Split next" is not possible in windows terminal without special configuration. Use "focus left/right/up/down" instead.'
        )

    def split_last():
        """Goes to last split"""
        # TODO: decide whether this notification is good style
        actions.app.notify(
            '"Split last" is not possible in windows terminal without special configuration. Use "focus left/right/up/down" instead.'
        )

    def split_number(index: int):
        """Navigates to a the specified split"""
        actions.app.notify(
            '"Split_number" is not possible in windows terminal in default configuration.'
        )

    def tab_final():
        actions.key("ctrl-alt-9")
