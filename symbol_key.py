from talon import Module, Context

mod = Module()
mod.list("my_symbol_key", desc="extra symbol keys")

ctx = Context()
ctx.lists["user.my_symbol_key"] = {
    "buck": "$",
    # "per": "%",
    "cent": "%",
    "low": "_",
    "eek": "=",
    # "is": "=",
    "bash": "\\",
    "wiggle": "~",
    "semi": ";",
    "lend": "(",
    "rend": ")",
    "lace": "}",
    "curl": "{",
    "whirl": "}",
    "fur": "}",
    "furl": "}",
    "face": "}",
    "bock": "[",
    "lock": "[",
    "lair": "[",
    "rock": "]",
    "rare": "]",
    "double": "\"",
    "dub": "\"",
    "single": "'",
}

@ctx.capture("user.symbol_key", rule="{user.symbol_key} | {user.my_symbol_key}")
def symbol_key(m):
    return str(m)
