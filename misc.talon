# dictate until keyword "over", in conjuction chose entry in dictation_mode.talon
# dictate [<phrase>]$:
#     mode.enable("dictation")
#     user.parse_phrase(phrase or "")

face on: mode.enable("user.my_face")
face off: mode.disable("user.my_face")
key(super-ctrl-enter): mode.toggle("user.my_face")
key(super-alt-enter):
    tracking.zoom_cancel()
    tracking.control_zoom_toggle(false)
	tracking.control_toggle()
key(super-alt-y): tracking.calibrate()
key(super-alt-u): user.reset_tobii()


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

talon edit config: user.system_command("codium {path.talon_user()}/bluedrink9-talon/")

# scout [<user.text>]: mimic("find it" + " {text or ''}")
# (jetpack | hunty | hunter) [<user.text>]: mimic("file hunt " + (text or ""))

brightness max: user.system_command("ddcutil setvcp 10 100")
brightness set <number>: user.system_command("ddcutil setvcp 10 {number}")
reset hub: user.system_command("sudo reset-tobii-hub")
reset toby: user.reset_tobii()

[mouse] nudge right [<number>]: mouse_nudge(number or 10, 0)
[mouse] nudge left [<number>]:
    number = number or 10
    mouse_nudge(-1*number, 0)
[mouse] nudge up [<number>]:
    number = number or 10
    mouse_nudge(0, -1*number)
[mouse] nudge down [<number>]: mouse_nudge(0, number or 10)

# deck(pedal_left): key(q)
# face(smile): key(enter)
