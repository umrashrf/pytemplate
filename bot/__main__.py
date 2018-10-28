import bot
import click


@click.group()
def cli():
    pass

@cli.command()
def gui():
    bot.main()

@cli.command()
def hello():
    print("hi there, everyone!")

cli()
