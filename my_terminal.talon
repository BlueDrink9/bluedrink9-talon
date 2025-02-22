tag: terminal
-
tag(): user.generic_unix_shell
# Say "core" before command:
# https://github.com/talonhub/community/blob/bd36d926861890113eb984be5e39947cdb5024c1/tags/terminal/unix_utility.talon-list
tag(): user.unix_utilities
tag(): user.git
# tag(): user.kubectl
tag(): user.readline

terminate: key(ctrl-c)
clear word left: key(ctrl-w)
clear line: key(ctrl-u)
complete: key(ctrl-e)
cancel [that]: key(ctrl-c)
