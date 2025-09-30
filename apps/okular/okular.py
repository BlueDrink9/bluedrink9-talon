from talon import Context, Module, actions


mod = Module()
ctx = Context()

mod.apps.okular = """
app.name: okular
"""

ctx.matches = r"""
app: okular
"""

ctx.tags = ["user.tabs"]

@ctx.action_class("app")
class TabActions:
    def tab_next():
        actions.key("ctrl-pagedown")

    def tab_previous():
        actions.key("ctrl-pageup")

    def tab_open():
        actions.key("ctrl-t")

    def tab_close():
        actions.key("ctrl-w")
