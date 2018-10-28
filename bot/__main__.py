import bot
import click
import logging

from pprint import pformat


@click.group()
def cli():
    pass

@cli.command()
def gui():
    bot.main()

@cli.command()
def hello():
    print("hi there, everyone!")
    logging.debug("Testing complex lines/data: \r" + pformat(dict(a=1,b=dict(),c="some big lines of data may be")))

cli()
