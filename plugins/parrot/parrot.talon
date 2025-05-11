mode: command
-

parrot(alveolar_click):
	print("alveolar_click")
    core.repeat_command(1)

parrot(cluck):
	print("cluck")
    key("enter")

parrot(throat_kh):
	print("throat_kh")
    edit.undo()

parrot(gutteral_ach):
	print("gutteral_ach")
    edit.undo()

parrot(shush:repeat):
	print("shush {power}")
    user.mouse_scroll_up(0)
    user.mouse_scroll_up(power * 0.05)
    # user.mouse_scroll_up_continuous()

# parrot(shush:stop):
#     user.scroll_stop_soft()

parrot(hiss:repeat):
	print("hiss {power}")
    user.mouse_scroll_down(0)
    user.mouse_scroll_down(power * 0.01)

parrot(unvoiced_th:repeat):
	print("unvoiced_th {power}")
    user.mouse_scroll_left(0)
    user.mouse_scroll_left(power * 0.01)

parrot(voiced_th:repeat):
	print("voiced_th {power}")
    user.mouse_scroll_right(0)
    user.mouse_scroll_right(power * 0.01)

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
# parrot(buzz):
# 	print("buzz")
