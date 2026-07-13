# TODO: Add indicator to tmux conf and change this to title matching, to set the app to tmux.
tag: terminal
# app: tmux
language: en
-
tag(): user.tmux

# Overrides for my custom bindings

mux previous window: user.tmux_keybind('ctrl-p')
mux next window: user.tmux_keybind('ctrl-n')

go split down | focus down: user.tmux_keybind('ctrl-j')
go split up | focus up: user.tmux_keybind('ctrl-k')
go split left | focus left: user.tmux_keybind('ctrl-h')
go split right | focus right: user.tmux_keybind('ctrl-l')
