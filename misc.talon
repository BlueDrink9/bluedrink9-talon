# dictate until keyword "over", in conjuction with entry in dictation_mode.talon
dictate [<phrase>]$:
    mode.enable("dictation")
    user.parse_phrase(phrase or "")
