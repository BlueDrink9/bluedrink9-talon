blast: edit.undo()
not that: edit.undo()
yes that: edit.redo()
do it: edit.redo()
remove: user.clear_last_phrase()
nope: user.clear_last_phrase()
scratcher: user.clear_last_phrase()

big junk: edit.delete_word()
bonk: edit.delete_word()
swallow:
    edit.extend_word_right()
    edit.delete()

billy: edit.word_left()
willie: edit.word_right()
pasty: edit.paste()
