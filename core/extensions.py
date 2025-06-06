from talon import Context, Module, actions

mod = Module()
ctx = Context()

mod.tag("extensions", desc="Enable extension commands")

# https://github.com/AndreasArvidsson/andreas-talon/blob/70371c9f64a7eaf9445ef220895e0bd5eb4ed9cd/core/extensions/extensions.py#L15
@mod.capture(rule="[{user.code_formatter}] <user.prose> [{user.file_extension}]")
def filename(m) -> str:
    try:
        text = actions.user.format_text(m.prose, m.code_formatter)
    except AttributeError:
        text = m.prose
    try:
        extension = m.extension
    except AttributeError:
        extension = ""
    return f"{text}{extension}"
