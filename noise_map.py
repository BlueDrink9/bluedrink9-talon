from talon import Module, actions, noise

noise_module = Module()

@noise_module.action_class
class NoiseActions:
    def noise_pop():
        """Invoked when the user does the pop noise."""
        pass

    def noise_hiss_start():
        """Invoked when the user starts hissing (potentially while speaking)"""
        pass

    def noise_hiss_stop():
        """Invoked when the user finishes hissing (potentially while speaking)"""
        pass


def hiss_handler(active):
    if active:
        pass
        # actions.key('shift')

def on_pop(active):
    pass

# noise.register("hiss", hiss_handler)
# noise.register("pop", on_pop)
# script cursor scrolling while hissing
from talon import ctrl, noise, cron
from time import sleep, time
from user.knausj_talon.code.mouse import start_cursor_scrolling, stop_scroll

start = 0
running = False
noise_length_threshold = "500ms"
threshold_passed = False

def still_running():
    global running
    global threshold_passed
    if running:
        threshold_passed = True
        start_cursor_scrolling()
        print('hiss duration passed threshold, starting gaze scroll')

def cursor_scroll_on_hiss(is_active):
  global start
  global running
  global threshold_passed
  if is_active:
    start = time()
    running = True
    cron.after(noise_length_threshold, still_running)
  else:
    running = False
    if threshold_passed:
        threshold_passed = False
        stop_scroll()
        print('end of hiss detected, disabling gaze scroll')


noise.register('hiss', cursor_scroll_on_hiss)
