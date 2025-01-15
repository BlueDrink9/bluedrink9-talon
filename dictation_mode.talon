# dictate until keyword "over", in conjuction with entry in misc.talon
mode: dictation
-
over [<phrase>]$:
    user.command_mode(phrase or "")
