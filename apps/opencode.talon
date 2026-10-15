tag: terminal
title: /OpenCode/i
-

# ----------------------------------------------------
# Palette & Navigation
# ----------------------------------------------------
please: key(ctrl-p)

# ----------------------------------------------------
# Session Management
# ----------------------------------------------------
session (new | clear): key(ctrl-x n)
session (compact | summarize): key(ctrl-x c)
session (list | resume | continue): key(ctrl-x l)
session export: key(ctrl-x x)
session share:
    insert("/share")
    key(enter)
session unshare:
    insert("/unshare")
    key(enter)

# ----------------------------------------------------
# Message History
# ----------------------------------------------------
message undo: key(ctrl-x u)
message redo: key(ctrl-x r)

# ----------------------------------------------------
# Models & Configuration
# ----------------------------------------------------
model (list | show): key(ctrl-x m)
model cycle: key(ctrl-t)
theme (list | show): key(ctrl-x t)
provider connect:
    insert("/connect")
    key(enter)

# ----------------------------------------------------
# UI Toggles
# ----------------------------------------------------
details toggle:
    insert("/details")
    key(enter)
thinking toggle:
    insert("/thinking")
    key(enter)

# ----------------------------------------------------
# Editor & Project Setup
# ----------------------------------------------------
editor open: key(ctrl-x e)
agent init:
    insert("/init")
    key(enter)
help show:
    insert("/help")
    key(enter)

# ----------------------------------------------------
# Application Lifecycle
# ----------------------------------------------------
(opencode | open code) (quit | exit): key(ctrl-x q)

# ----------------------------------------------------
# Input Prefixes
# ----------------------------------------------------
file reference: insert("@")
shell run: insert("!")
command run: insert("/")
