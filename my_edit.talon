blast: edit.undo()
not that: edit.undo()
yes that: edit.redo()
do it: edit.redo()
big wipe: key(ctrl-w)
big junk: key(ctrl-w)
remove: user.clear_last_phrase()

scratcher:
    edit.extend_word_left()
    edit.delete()
swallow:
    edit.extend_word_right()
    edit.delete()
