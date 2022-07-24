#! /usr/bin/env python3

import click

@click.group()
def cli():
  pass

@click.command()
@click.option('-c', '--count', default=1, type=int, help='number of records')
@click.option('-n', '--name',  default='test', help='database name')
@click.option('-u', '--user', help='user from environment', envvar='USER')
@click.option('-d', '--srcdir', help='user from environment', envvar='HOME')
def initdb(count, user, name, srcdir):
  click.echo(f"Intialized {user} database {name} {count} times in {srcdir}")

@click.command()
def dropdb():
  click.echo('Dropped the database')

cli.add_command(initdb)
cli.add_command(dropdb)

if __name__ == '__main__':
  cli()
