from talon import Module, Context

mod = Module()
mod.list("my_symbol_key", desc="extra symbol keys")

ctx = Context()
ctx.lists["user.my_symbol_key"] = {
    "wiggle": "~",
    "semi": ";",
    "lend": "(",
    "rend": ")",
    "curl": "{",
    "whirl": "}",
    "furl": "}",
    "face": "}",
    "lox": "[",
    "rox": "]",
    "rare": "]",
    "double": "\"",
    "dub": "\"",
    "single": "'",
}

@ctx.capture("user.symbol_key", rule="{user.symbol_key} | {user.my_symbol_key}")
def symbol_key(m):
    return str(m)
