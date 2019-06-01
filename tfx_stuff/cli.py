"""Command line interface for tfx_stuff"""
import click

from tfx_stuff import main


@click.command()
@click.option('-v', '--verbose', count=True)
@click.option('--option', default='default_val', help='An example optional parameter')
def cli(option, verbose):
    click.echo(click.style('Hello tfx_stuff!', fg='magenta', bold=True))
    click.echo('Verbosity level: {}'.format(verbose))
    click.echo('Optional param: {}'.format(option))
    result = main.main()
    click.echo('Main output: {}'.format(result))
