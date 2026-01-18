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

parrot(pop):
	print("pop")
    # tracking.zoom_cancel()
    do_zoom = tracking.control_zoom_enabled()
    do_click = user.not_(do_zoom)
    print(do_zoom)
    if do_click: mouse_click(0)
    # if do_zoom: tracking.zoom()

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
    tracking.zoom_cancel()
    user.scroll("right", power)

parrot(voiced_th:stop):
    user.scroll_stop_soft()

parrot(unvoiced_th:repeat):
	print("unvoiced_th {power}")
    tracking.zoom_cancel()
    user.scroll("left", power)

parrot(unvoiced_th:stop):
    user.scroll_stop_soft()

parrot(lip_buzz):
	print("buzz")
    tracking.zoom_cancel()
	tracking.control_toggle()

parrot(falsetto_squeak):
    print("squeak")
    # close zoom if open
    tracking.zoom_cancel()
    user.mouse_drag(0)
    # close the mouse grid if open
    user.grid_close()

parrot(whistle):
    print("whistle")
    # close zoom if open
    tracking.zoom_cancel()
    mouse_click(1)
    # close the mouse grid if open
    user.grid_close()

# parrot(falsetto_squeak):
#     print("squeak")
#     # close zoom if open
#     tracking.zoom_cancel()
#     mouse_click(1)
#     # close the mouse grid if open
#     user.grid_close()

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
