# Why does this file exist, and why not put this in `__main__`?
#
# You might be tempted to import things from `__main__` later,
# but that will cause problems: the code will get executed twice:
#
# - When you run `python -m ihtt` python will execute
#   `__main__.py` as a script. That means there won't be any
#   `ihtt.__main__` in `sys.modules`.
# - When you import `__main__` it will get executed again (as a module) because
#   there's no `ihtt.__main__` in `sys.modules`.

"""Module that contains the command line application."""

import typer


def main() -> int:
    typer.echo("I Hate Time Tracking — CLI")
    return 0
