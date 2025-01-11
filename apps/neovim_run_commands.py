from talon import Context, Module, actions, app, settings, ui

from importlib import import_module

VimAPI = import_module(".neovim-talon.core.rpc.api", package="user").VimAPI
VimMod = import_module(".neovim-talon.core.rpc.modes", package="user").VimMode

mod = Module()


@mod.action_class
class Actions:
    def vim_run_insert(cmd: str):
        """run a given list of commands in normal mode, preserve mode"""
        actions.user.vim_set_insert()
        cmd = cmd.replace(":", ";")
        actions.insert(cmd)

    def vim_run_insert_key(cmd: str):
        """run a given list of commands in normal mode, preserve mode"""
        actions.user.vim_set_insert()
        cmd = cmd.replace(":", ";")
        actions.key(cmd)

    def vim_run_normal(cmd: str):
        """run a given list of commands in normal mode, preserve INSERT"""
        # XXX - This needs to be abstracted for the case where we don't have
        # RPC
        # This is required despite using the nvim.command() method because we
        # can access that mode from terminal mode:
        #  https://github.com/neovim/neovim/issues/4895#issuecomment-303073838
        if actions.user.vim_is_terminal():
            actions.user.vim_set_normal_exterm()
        vapi = VimAPI()
        cmd = cmd.replace(":", ";")
        vapi.api.run_normal_mode_command(cmd)

    def vim_run_normal_np(cmd: str):
        """run a given list of commands in normal mode, don't preserve
        INSERT"""
        actions.user.vim_set_normal_np()
        cmd = cmd.replace(":", ";")
        actions.insert(cmd)

    def vim_run_normal_exterm(cmd: str = None):
        """run a given list of commands in normal mode, don't preserve INSERT,
        escape from terminal mode"""
        actions.user.vim_set_normal_exterm()
        if cmd is not None:
            cmd = cmd.replace(":", ";")
            actions.insert(cmd)

    def vim_run_normal_key(cmd: str):
        """press a given key in normal mode"""
        actions.user.vim_set_normal()
        cmd = cmd.replace(":", ";")
        actions.key(cmd)

    def vim_run_normal_exterm_key(cmd: str):
        """press a given key in normal mode, and escape terminal"""
        actions.user.vim_set_normal_exterm()
        cmd = cmd.replace(":", ";")
        actions.key(cmd)

    def vim_run_normal_keys(keys: str):
        """press a given list of keys in normal mode"""
        actions.user.vim_set_normal()
        keys = keys.replace(":", ";")
        for key in keys.split(" "):
            actions.key(key)

    def vim_run_normal_exterm_keys(keys: str, term_return: str = "False"):
        """press a given list of keys in normal mode"""
        v = actions.user.vim_set_normal_exterm()
        keys = keys.replace(":", ";")
        for key in keys.split(" "):
            actions.key(key)
        if term_return == "True":
            v.set_insert_mode()

    def vim_run_visual(cmd: str):
        """run a given list of commands in visual mode"""
        actions.user.vim_set_visual()
        cmd = cmd.replace(":", ";")
        actions.insert(cmd)

    def vim_run_command(cmd: str):
        """run string of commands in command line mode.

        Preserves INSERT
        """
        vapi = VimAPI()
        cmd = cmd.replace(":", ";")
        vapi.api.run_command_mode_command(cmd)

    def vim_run_command_exterm(cmd: str):
        """run string of commands in command line mode.

        - Preserves INSERT
        - Exits terminal mode
        """
        vapi = VimAPI()
        cmd = cmd.replace(":", ";")
        vapi.api.run_command_mode_command_exterm(cmd)

    # Sometimes the .talon file won't know what mode to run something in, just
    # that it needs to be a mode that supports motions like normal and visual.
    def vim_run_any_motion(cmd: str):
        """run a given list of commands in normal mode"""
        actions.user.vim_set_any_motion_mode()
        cmd = cmd.replace(":", ";")
        actions.insert(cmd)

    # Sometimes the .talon file won't know what mode to run something in, just
    # that it needs to be a mode that supports motions like normal and visual.
    def vim_run_any_motion_exterm(cmd: str):
        """run a given list of commands in some motion mode"""
        actions.user.vim_set_any_motion_mode_exterm()
        cmd = cmd.replace(":", ";")
        actions.insert(cmd)

    def vim_run_any_motion_key(cmd: str):
        """run a given list of commands in normal mode"""
        actions.user.vim_set_any_motion_mode()
        cmd = cmd.replace(":", ";")
        actions.key(cmd)

    def vim_run_any_motion_exterm_key(cmd: str):
        """run a given list of commands in normal mode"""
        actions.user.vim_set_any_motion_mode_exterm()
        cmd = cmd.replace(":", ";")
        actions.key(cmd)
