tag: user.build123d
-

{user.build123d_function}: user.insert_between(build123d_function + "(", ")")
{user.build123d_enum}: insert(build123d_enum)

<user.build123d_positioning>: insert(build123d_positioning)

show all:
    user.run_rpc_command("workbench.debug.action.focusRepl")
    insert("show_all()")
    key(enter)

origin: "(0, 0, 0)"
origin two: "(0, 0)"
direction zed: "(0, 0, 1)"
direction ex: "(1, 0, 0)"
direction why: "(0, 1, 0)"
direction minus zed: "(0, 0, -1)"
direction minus ex: "(-1, 0, 0)"
direction minus why: "(0, -1, 0)"

op at: " @ "
op tangent: " % "
