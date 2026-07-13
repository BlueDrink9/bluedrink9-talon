os: linux
and app.name: DB Browser for SQLite
-
tag(): user.tabs
tag(): user.sql
settings():
    # Ensure selecting by typing (eg for tables) works - pasting doesn't select the pasted text.
    user.paste_to_insert_threshold = 25

    # insert_wait = 10
    # hotkey_wait = 10
    # key_wait = 10

table next: key(ctrl-pagedown)
table previous: key(ctrl-pageup)
table select:
    # Go to table dropdown - First opened the file menu to avoid opening the tools menu
    key(alt-f)
    sleep(0.1)
    key(escape escape)
    sleep(0.1)
    key(alt-t)
    sleep(0.1)
    key(alt-down)
table select <phrase>:
    # Go to table dropdown - First opened the file menu to avoid opening the tools menu
    key(alt-f)
    sleep(0.1)
    key(escape escape)
    sleep(0.1)
    key(alt-t)
    sleep(0.1)
    key(alt-down)
    sleep(0.1)
    insert(phrase)
    sleep(0.1)
    key(enter)

value set null: key(alt-delete)
value set blank: key(delete)
record delete: key(alt-delete)
record blank: key(delete)
cell edit | value edit: key(f2)

query run: key(ctrl+enter)
query run line: key(shift-f5)

record duplicate: key("ctrl-\"")

reload it: key(f5)

filter this: key(ctrl-shift-f)
filter all: key(ctrl-alt-f)

line run: key(shift-f5)
file run | query run: key(ctrl-enter)

database structure: key(alt-1)
browse data: key(alt-2)
edit pragmas: key(alt-3)
execute sequel: key(alt-4)

view toggle log: key(ctrl-L)
view toggle plot: key(ctrl-D)
view toggle schema: key(ctrl-I)

column select: key(ctrl-space)
row select: key(shift-space)
