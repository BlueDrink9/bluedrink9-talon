tag: user.build123d
-

{user.build123d_function}: user.insert_between(build123d_function + "(", ")")
{user.build123d_enum}: insert(build123d_enum)

<user.build123d_positioning>: insert(build123d_positioning)

show all:
    user.run_rpc_command("workbench.debug.action.focusRepl")
    insert("show_all()")
    key(enter)
