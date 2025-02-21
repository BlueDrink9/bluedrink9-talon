from talon import Module, Context, actions, app
import subprocess

mod = Module()
ctx = Context()
mod.tag("send", desc="Tag for apps that use vim motions to send lines to repl")
