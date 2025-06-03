mode: command
-

parrot(alveolar_click):
	print("alveolar_click")
    core.repeat_command(1)

parrot(kiss):
	print("kiss")
    key("enter")

parrot(cluck):
	print("cluck")
    edit.undo()

# parrot(throat_kh):
# 	print("throat_kh")
#     edit.undo()

parrot(guttural_ach):
	print("gutteral_ach")
    edit.undo()

parrot(shush:repeat):
	print("shush {power}")
    tracking.zoom_cancel()
    user.scroll("up", power)

parrot(shush:stop):
    user.scroll_stop_soft()

parrot(hiss:repeat):
	print("hiss {power}")
    tracking.zoom_cancel()
    user.scroll("down", power)

parrot(hiss:stop):
    user.scroll_stop_soft()

parrot(voiced_th:repeat):
	print("voiced_th {power}")
    user.scroll("right", power)

parrot(voiced_th:stop):
    user.scroll_stop_soft()

parrot(unvoiced_th:repeat):
	print("unvoiced_th {power}")
    user.scroll("left", power)

parrot(unvoiced_th:stop):
    user.scroll_stop_soft()

parrot(lip_buzz):
	print("buzz")

parrot(falsetto_squeak):
	print("falsetto_squeak")

# parrot(hiss:stop):
#     user.mouse_scroll_stop()

# parrot(palate_click):
# 	print("palate_click")

# parrot(gluck):
# 	print("gluck")

# parrot(finger_snap):
# 	print("finger_snap")

# parrot(horse):
# 	print("horse")

# parrot(whistle):
# 	print("whistle")
