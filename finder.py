#!/usr/bin/env python

from mylib.walk import walk
import click

#build click group
@click.group()
def cli():
    """finds patterns"""

#build click command
@cli.command("discover")
@click.option("--path", default="/workspaces/assimilate-python-from-zero/assets", help="path to search")
@click.option("--pattern", default=None, help="pattern to searc default is audio and video files")
@click.option("--ignore", default=".hidden", help="pattern to ignore")
def discover(path, pattern, ignore):
    """finds patterns"""
    for p in walk(path, pattern, ignore):
        print(p)

if __name__ == "__main__":
    cli()