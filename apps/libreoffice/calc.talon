app: libre_office
-

go <user.letter> <user.number_string>:
    # Open navigator sidebar
    key(alt-4)
    sleep(20ms)
    # Delete existing letters
    key(ctrl-delete)
    insert(letter)
    key(tab tab)
    insert(number_string)
    key(enter)
    # Close sidebar
    key(ctrl-f5)

Reload it: key(alt-f l)
filter all: key(ctrl-shift-l)
filter this: key(alt-down)
filter change: key(alt-down)
delete cells: key(ctrl--)
insert cells: key(ctrl-+)
column hide: key(alt-o m h)
freeze top row: key(alt-v c r)
freeze first column: key(alt-v c f)
select visible columns: key(alt-e e o)
select visible rows: key(alt-e e v)

edit: key(f2)


box top left:
    key(ctrl-home)

box bottom right:
    key(ctrl-end)

box home:
    key(home)

box end:
    key(end)

box left:
    key(ctrl-left)

box right:
    key(ctrl-right)

box up:
    key(ctrl-up)

box down:
    key(ctrl-down)

take home:
    key(shift-home)

take end:
    key(shift-end)

take box left:
    key(ctrl-shift-left)

take box right:
    key(ctrl-shift-right)

take box down:
    key(ctrl-shift-down)

take box up:
    key(ctrl-shift-up)

take row:
    key(shift-space)

take column:
    key(ctrl-space)

take range:
    key(ctrl-*)

sheet left:
    key(ctrl-pgup)

sheet right:
    key(ctrl-pgdown)

screen left:
    key(alt-pgup)

screen right:
    key(alt-pgdown)

# taken from excel shortcuts
column select: key(ctrl-space)
column insert: key(ctrl-space ctrl-shift-=)
column delete: key(ctrl-space ctrl--)
column top: key(ctrl-up)
column bottom: key(ctrl-down)
column fit: key(alt-h o i)
column filter: key(ctrl-down ctrl-up alt-down)
column width: key(alt-h o w)

row select: key(shift-space)
row insert: key(shift-space ctrl-shift-=)
row delete: key(shift-space ctrl--)
row start: key(ctrl-left)
row end: key(ctrl-right)
row fit: key(alt-h o a)
row height: key(alt-h o h)

table select: key(ctrl-a)
select all: key(ctrl-a:3)

sheet new: key(shift-f11)
sheet previous: key(ctrl-pageup)
sheet next: key(ctrl-pagedown)
sheet rename: key(alt-h o r)
