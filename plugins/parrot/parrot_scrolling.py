# https://github.com/rokubop/parrot_mode_14_noise_v6/blob/main/src/scrolling.py
from enum import Enum
from talon import cron, settings, actions, Module, Context
import time
import math
from typing import Callable

mod = Module()

mod.setting(
    name="parrot_mouse_scroll_scale",
    type=float,
    default=0.06,
    desc="Setting for parrot mouse base scroll speed multiplier",
)

mod.setting(
    name="parrot_mouse_scroll_power_scale",
    type=float,
    default=50,
    desc="Setting to scale parrot mouse scroll speed based on max power. This value is the power that would scroll 20 lines * parrot_mouse_scroll_scale",
)

class ScrollDirection(Enum):
    UP = "up"
    DOWN = "down"
    LEFT = "left"
    RIGHT = "right"


class Scrolling:
    def __init__(self):
        self.scroll_job = None
        self.scroll_dir = ScrollDirection.UP
        self.noise_power = 1
        self.scroll_start_ts: float = 0.0
        self.scroll_stop_soft_ts: float = 0.0
        self.last_tick_ts = -math.inf
        # scroll only every n seconds
        self.min_tick_interval = 0.1
        self.debounce_start_duration = 0.0
        self.debounce_stop_duration = 0.170
        self.scroll_stop_soft_callbacks = []
        self.__power_scale_target_coef = None

    def scroll_start(self, direction: str, power: float = 1):
        """Start scrolling until stop is called"""
        new_scroll_dir = ScrollDirection[direction.upper()]
        self.scroll_stop_soft_ts = 0.0

        self.noise_power = power
        if self.scroll_job:
            if new_scroll_dir != self.scroll_dir:
                self.scroll_dir = new_scroll_dir
                self.scroll_start_ts = time.perf_counter()
            # scroll_job already exists
            return

        self.scroll_dir = new_scroll_dir
        self.scroll_start_ts = time.perf_counter()
        self._scroll_tick()
        self.scroll_job = cron.interval("16ms", self._scroll_tick)

    def _scroll_tick(self):
        ts = time.perf_counter()
        s_since_start = ts - self.scroll_start_ts
        if s_since_start < self.debounce_start_duration:
            return

        # Only tick every n seconds
        s_since_last_tick = ts - self.last_tick_ts
        if s_since_last_tick < self.min_tick_interval:
            return
        self.last_tick_ts = ts

        if (
            self.scroll_stop_soft_ts
            and ts - self.scroll_stop_soft_ts > self.debounce_stop_duration
        ):
            self.scroll_stop_hard()
            if self.scroll_stop_soft_callbacks:
                for callback in self.scroll_stop_soft_callbacks:
                    callback()
            return

        # Initial acceleration gradually increases for the first 0.5 seconds
        acceleration_speed = 1 + min(s_since_start / 0.5, 4)
        x, y = 0, 0
        power = max(1, (
            settings.get("user.parrot_mouse_scroll_scale")
            * acceleration_speed
            * self._scale_power()
        ))
        print(power, self.scroll_stop_soft_ts, self.scroll_start_ts, ts)
        match self.scroll_dir:
            case ScrollDirection.UP:
                y = -power
            case ScrollDirection.DOWN:
                y = power
            case ScrollDirection.LEFT:
                x = -power
            case ScrollDirection.RIGHT:
                x = power
        print(f"scrolling {self.scroll_dir} * {power}")
        actions.mouse_scroll(x=x, y=y, by_lines=True)

    def scroll_stop_soft(self):
        self.scroll_stop_soft_ts = time.perf_counter()

    def scroll_stop_hard(self):
        self.scroll_start_ts = 0.0
        self.scroll_stop_soft_ts = 0.0
        if self.scroll_job:
            cron.cancel(self.scroll_job)
            self.scroll_start_ts = 0.0
            self.scroll_stop_soft_ts = 0.0
            self.scroll_job = None

    def is_scrolling(self):
        return self.scroll_job is not None

    def register_scroll_stop_soft_callback(self, callback: Callable[[], None]):
        self.scroll_stop_soft_callbacks.append(callback)

    def clear_scroll_stop_soft_callbacks(self):
        self.scroll_stop_soft_callbacks.clear()

    def _scale_power(self):
        if not self.__power_scale_target_coef:
            power_scale_target_lines = 20
            self.__power_scale_target_coef = (
                (power_scale_target_lines - 1) /
                    math.log(settings.get("user.parrot_mouse_scroll_power_scale"))
            )
        return (
            self.__power_scale_target_coef * math.log(self.noise_power) + 1
        )

scrolling = Scrolling()


@mod.action_class
class Actions:
    def scroll_stop_soft():
        """Stop scrolling, but keep the scroll job alive"""
        scrolling.scroll_stop_soft()

    def scroll(dir: str, power: float):
        """Scroll in the given direction"""
        scrolling.scroll_start(dir, power=power)
