from talon import Module, Context, actions

mod = Module()
# Context valid for most modes
ctx = Context()
ctx.matches = r"""
app: neovim
and not tag: user.vim_mode_command
"""
# and user.neovim_plugin: session


@mod.action_class
class Actions:
    def open_session(name: str):
        """ :OpenSession """
        if name:
            actions.user.vim_run_command(f":OpenSession {name}\n")
        else:
            actions.user.vim_run_command(":OpenSession")
