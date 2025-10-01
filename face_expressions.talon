mode: face
-
# All raw expressions: brow_down_left, brow_down_right, brow_inner_up, brow_outer_up_left, brow_outer_up_right, blink_left, blink_right, gaze_down_left, gaze_down_right, gaze_in_left, gaze_in_right, gaze_out_left, gaze_out_right, gaze_up_left, gaze_up_right, squint_left, squint_right, eye_wide_left, eye_wide_right, jaw_open, jaw_left, jaw_right, mouth_close, dimple_left, dimple_right, frown_left, frown_right, mouth_funnel, mouth_lower_down_left, mouth_lower_down_right, mouth_press_left, mouth_press_right, mouth_pucker, mouth_right, mouth_left, mouth_roll_lower, mouth_roll_upper, mouth_shrug_lower, mouth_shrug_upper, smile_left, smile_right, mouth_stretch_left, mouth_stretch_right, mouth_upper_up_left, mouth_upper_up_right

face(brow_outer_up_right): mouse_click(0)
face(jaw_open:repeat):
    user.mouse_scroll_down()
    mouse_scroll(1, 0, true)
    sleep(0.1)
face(smile:repeat):
    mouse_scroll(-1, 0, true)
    sleep(0.1)


face(blink): print("blink")
# The left and right recognition seems backwards for mouth stretch
# face(mouth_stretch_left): user.system_command("bspc desktop -f next.local")
# face(mouth_stretch_right): user.system_command("bspc desktop -f prev.local")
face(frown_left): print("frown_left")
face(frown_right): print("frown_right")
face(eye_wide_left): print("eye_wide_left")
face(eye_wide_right): print("eye_wide_right")
face(mouth_close): print("mouth_close")
face(mouth_roll_lower): print("mouth_roll_lower")
# face(gaze_up_right): print("gaze_up_right")
# face(gaze_out_left): print("gaze_out_left")
# face(gaze_out_right): print("gaze_out_right")
