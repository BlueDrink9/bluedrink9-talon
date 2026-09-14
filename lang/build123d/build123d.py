from talon import Context, Module, actions

mod = Module()

# Declare the mode and tag in the user namespace
# mod.mode("cad", desc="CAD mode")
mod.tag("build123d", desc="Tag for build123d DSL voice commands")
mod.list("build123d_positions", desc="Position terms for build123d")

# Automatically activate the tag when CAD mode is active
ctx = Context()
ctx.matches = r"""
code.language: python
"""

@mod.action_class
class Actions:
    def build123d_tag_toggle():
        """Toggle the build123d tag on or off"""
        pass

    def build123d_tag_on():
        """Toggle the build123d tag on"""
        pass

    def build123d_tag_off():
        """Toggle the build123d tag off"""
        pass

@ctx.action_class("user")
class Actions:
    def build123d_tag_toggle():
        """Toggle the build123d tag on or off"""
        if "user.build123d" in ctx.tags:
            ctx.tags = []
        else:
            ctx.tags = ["user.build123d"]

    def build123d_tag_on():
        ctx.tags = ["user.build123d"]

    def build123d_tag_off():
        ctx.tags = []

@mod.capture(rule="[all] {user.build123d_positions}+ [all]")
def build123d_positioning(m) -> str:
    """Captures 1+ positioning terms with optional 'all' before or after."""
    # Check if 'all' was spoken in the phrase
    has_all = "all" in m

    # Join captured positioning terms into a phrase
    phrase = "_".join(m.build123d_positions_list)

    suffix = "(ALL)" if has_all else "()"
    return f"{phrase}{suffix}"
