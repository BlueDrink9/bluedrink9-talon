from talon import Module, actions, noise, ctrl, cron
from time import sleep, time

noise_module = Module()

noise_length_threshold = 500 # ms

start = 0
running = False
threshold_passed = False

@noise_module.action_class
class NoiseActions:

    # def noise_pop():
    #     """Invoked when the user does the pop noise."""
    #     pass

    def noise_hiss_start():
        """Invoked when the user starts hissing (potentially while speaking)"""
        NoiseActions.cursor_scroll_on_hiss(True)

    # script cursor scrolling while hissing
    def still_hissing():
        """If we haven't stopped hissing since starting the timer, start scrolling down"""
        global running
        global threshold_passed
        global start
        if running and time() - start > noise_length_threshold:
            print('hiss duration passed threshold, starting gaze scroll')
            threshold_passed = True
            actions.user.mouse_scroll_down_continuous()

    def cursor_scroll_on_hiss(is_active: bool):
        """Start timer that will initiate cursor scrolling on hiss, if the hiss length passes the threshold"""
        global start
        global running
        global threshold_passed
        # Only if this is a continuous hiss. If already running the timer,
        # don't start a new one.
        if running:
            return
        start = time()
        running = True
        print('Starting a hiss scroll timer')
        for interval in [noise_length_threshold]:
            cron.after(str(interval) + "ms", NoiseActions.still_hissing)

    def cursor_hiss_scroll_stop():
        """Stop the hiss running - indicate it was not continuous, and stop scrolling if currently doing so"""
        global running
        global threshold_passed
        running = False
        print('end of hiss detected, disabling gaze scroll')
        threshold_passed = False
        actions.user.mouse_scroll_stop()

    def noise_hiss_stop():
        """Invoked when the user finishes hissing (potentially while speaking)"""
        NoiseActions.cursor_hiss_scroll_stop()


def hiss_handler(active):
    if active:
        NoiseActions.noise_hiss_start
    else:
        NoiseActions.noise_hiss_stop

def on_pop(active):
    pass

# noise.register("hiss", hiss_handler)
# noise.register("pop", on_pop)
