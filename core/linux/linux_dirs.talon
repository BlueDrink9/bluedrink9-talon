# linux_navigation.terminal.talon
tag: terminal
-

# Commands to use the list for cd or inserting paths
go deer {user.linux_dir}:
    insert("cd " + user.linux_dir)
    key(enter)

deer {user.linux_dir}:
    insert(user.linux_dir)

lisa deer {user.linux_dir}:
    insert("ls " + user.linux_dir)
    key(enter)
