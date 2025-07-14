app: libre_office
-

go <user.letters> <user.number_string>:
    # Open navigator sidebar
    key(alt-4)
    sleep(20ms)
    # Delete existing letters
    key(ctrl-delete)
    insert(letters)
    key(tab tab)
    insert(number_string)
    key(enter)
    # Close sidebar
    key(ctrl-f5)

Reload it: key(alt-f l)
filter all: key(ctrl-shift-l)
filter this: key(alt-down)
filter change: key(alt-down)
filter clear:
    key(alt-down)
    key(shift-tab)
    insert("clear")
    key(enter)
filter [column|this] to [just|only] (<user.text>|empty):
    key(escape)
    # Ensure we are at the top of the column
    key(ctrl-up:10)
    key(alt-down)
    # Toggle 'all' to blank
    key(alt-a)
    # Focus list
    key(tab:4)
    # Jump to text
    insert(text or "(empty)")
    key(space)
    # Ok
    key(alt-o)

filter [column|this] [except|to not] (<user.text>|empty):
    key(escape)
    # Ensure we are at the top of the column
    key(ctrl-up:10)
    key(alt-down)
    # # Toggle 'all' to blank
    # key(alt-a)
    # Focus list
    key(tab:4)
    # Jump to text
    insert(text or "(empty)")
    key(space)
    # Ok
    key(alt-o)

delete cells: key(ctrl--)
delete row: key(alt-s u)
delete column: key(alt-s o)

insert cells: key(ctrl-+)
column hide: key(alt-o m h)
freeze top row: key(alt-v c r)
freeze first column: key(alt-v c f)
select visible columns: key(alt-e e o)
select visible rows: key(alt-e e v)
sort ascending: key(alt-d a)
sort descending: key(alt-d n)

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
complete: key(alt-down)
column select: key(ctrl-space)
column copy: key(escape ctrl-space ctrl-c)
column insert: key(ctrl-space ctrl-shift-=)
column delete: key(ctrl-space ctrl--)
column top: key(ctrl-up)
column bottom: key(ctrl-down)
column fit: key(alt-h o i)
column filter: key(ctrl-down ctrl-up alt-down)
column width: key(alt-h o w)

row select: key(shift-space)
row copy: key(escape shift-space ctrl-c)
row insert: key(shift-space ctrl-shift-=)
insert row below: key(alt-s r b)
insert row above: key(alt-s r a)
insert column left: key(alt-s r b)
insert column right: key(alt-s r a)
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

paste special: key(ctrl-alt-v)
paste transposed: key(alt-e s t)
