# dictate until keyword "over", in conjuction chose entry in dictation_mode.talon
# dictate [<phrase>]$:
#     mode.enable("dictation")
#     user.parse_phrase(phrase or "")

send (that|it): insert(" ss")

send selection: insert(" s")

beat: sleep(1)

tut: ""
tuss: ""

choose yes: key(alt-y)
choose no: key(alt-n)
choose okay: key(alt-o)
choose cancel: key(alt-c)
big clap: key(ctrl-enter)
clapper: key(ctrl-enter)
pinger: key(ctrl-enter)

cody |coda | coder: user.switcher_focus("Codium")
foxy: user.switcher_focus("firefox")
kitty: user.switcher_focus("kitty")

# scout [<user.text>]: mimic("find it" + " {text or ''}")
# (jetpack | hunty | hunter) [<user.text>]: mimic("file hunt " + (text or ""))

brightness max: user.system_command("ddcutil setvcp 10 100")
brightness set <number>: user.system_command("ddcutil setvcp 10 {number}")

mouse nudge right [<number>]: mouse_nudge(number or 10, 0)
mouse nudge left [<number>]: mouse_nudge(-(number or 10), 0)
mouse nudge up [<number>]: mouse_nudge(0, -(number or 10))
mouse nudge down [<number>]: mouse_nudge(0, number or 10)
