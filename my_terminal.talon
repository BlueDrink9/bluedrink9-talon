tag: terminal
language: en
-
tag(): user.generic_unix_shell
# Say "core" before command:
# https://github.com/talonhub/community/blob/bd36d926861890113eb984be5e39947cdb5024c1/tags/terminal/unix_utility.talon-list
tag(): user.unix_utilities
tag(): user.git
# tag(): user.kubectl
tag(): user.readline_vi

terminate: key(ctrl-c)
clear word left: key(ctrl-w)
complete: key(ctrl-e)
cancel [that]: key(ctrl-c)
# Clear line, exit scrollbacks etc, before running last
rerun last:
    key(ctrl-c:2 up enter)
code: "code "
editor | edit | edd: "e "
are script: "Rscript "

dvc: "dvc "
dvc status: "dvc status\n"
dvc add: "dvc add "

system control: "systemctl "
system control status: "systemctl status "
system control start: "systemctl start "
system control stop: "systemctl stop "
system control restart: "systemctl restart "
system control enable: "systemctl enable "
system control disable: "systemctl disable "
system control list: "systemctl list-units --type=service --all\n"
system control logs: "journalctl -u "
