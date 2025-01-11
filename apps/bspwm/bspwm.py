from talon import Module, Context, actions, app
import subprocess

mod = Module()
ctx = Context()

mod.list("bspwm_verb", desc="BSPWM verbs")
mod.list("bspwm_noun", desc="BSPWM nouns")
mod.list("bspwm_direction", desc="BSPWM directions")

ctx.lists["user.bspwm_verb"] = {
    "go": "--focus",
    "move to monitor": "--to-monitor",
    "swap": "--swap",
    "close": "--close",
    "kill": "--kill",
    "remove": "--remove",
}
ctx.lists["user.bspwm_noun"] = {
    "workspace": "desktop",
    "desk": "desktop",
    "node": "node",
    "window": "node",
    "monitor": "monitor",
}
numbers = {
    str(i): str(i) for i in range(1, 11)
}
ctx.lists["user.bspwm_direction"] = {
    "left": "left",
    "right": "right",
    "up": "up",
    "down": "down",
    "prev": "prev",
    "next": "next",
    # TODO: maybe convert this to a capture so use actual user.numbers.
    # As-is, this tries to read utterance "1", which is nonsence.
} | numbers

# Direction mappings
direction_mappings = {
    "node": {
        "left": "west",
        "right": "east",
        "up": "north",
        "down": "south",
    },
    "desktop": {
        "left": "prev",
        "right": "next",
    },
    "monitor": {
        "left": "prev",
        "right": "next",
    },
}

resize_actions = {
    "bigger": ("grow", "10"),
    "smaller": ("shrink", "10"),
}

def bspc_command(*args: str):
    """Execute a bspc command."""
    args = [item for item in args if item not in [""]]
    result = subprocess.run(["bspc", *args], capture_output=True)
    if result.stderr:
        raise subprocess.CalledProcessError(
                returncode = result.returncode,
                cmd = result.args,
                stderr = result.stderr
                )
    if result.stdout:
        print("Command Result: {}".format(result.stdout.decode('utf-8')))
    # actions.user.system_command_nb("bspc" + " ".join(args))

@mod.action_class
class Actions:

    def bspwm_action(command: str, noun: str, selector: str):
        """Handle a generic bspwm action."""
        # Handle numbers (e.g., workspace 1, monitor 2)
        if selector.isdigit():
            if noun == "workspace":
                bspc_command(noun, command, f"^{selector}")
            elif noun == "monitor":
                bspc_command(noun, command, f"^@^{selector}")
            return

        # Handle direction-specific mappings
        if selector in direction_mappings.get(noun, {}):
            mapped_param = direction_mappings[noun][selector]
            if not mapped_param:
                app.notify(f"No mapping for {selector} with noun {noun}")
                return
            bspc_command(noun, command, mapped_param)

        # Handle swap or resize actions
        elif command == "resize" and selector in resize_actions:
            action, amount = resize_actions[selector]
            bspc_command(noun, command, action, amount)

        else:
            bspc_command(noun, command, selector)
