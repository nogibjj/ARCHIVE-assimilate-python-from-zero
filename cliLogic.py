#!/usr/bin/env python

import click
from random import choice
from mylib.logic import random_fruit

# build a click group
@click.group()
def cli():
    """This is a cli tool that runs code in the mylib package"""


# build a click command
@cli.command("randofruit")
# add a click option
@click.option("--count", default=1, help="Number of fruits to generate")
def random_fruit_command(count):
    """Print a bunch of random fruits.

    Example:
        ./cli.py randofruit --count 5
    """

    for _ in range(count):
        # randomly print a new colored fruit
        colors = ["red", "green", "yellow", "blue", "magenta", "cyan", "white"]
        click.secho(next(random_fruit()), fg=choice(colors))


# run the cli
if __name__ == "__main__":
    cli()
