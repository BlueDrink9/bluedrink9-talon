# dictate until keyword "over", in conjuction with entry in dictation_mode.talon
# dictate [<phrase>]$:
#     mode.enable("dictation")
#     user.parse_phrase(phrase or "")

send (that|it): insert(" ss")

send selection: insert(" s")

over: ""
big clap: key(ctrl-enter)
clapper: key(ctrl-enter)

cody |coda | coder: mimic("focus codium")
foxy: mimic("focus firefox")
kitty: mimic("focus kitty")

scout: mimic("find it")
jetpack | hunty | hunter: mimic("file hunt")
brightness max: user.system_command("ddcutil setvcp 10 100")
brightness set <number>: user.system_command("ddcutil setvcp 10 {number}")
