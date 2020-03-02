#!/usr/bin/env python
import click

@click.command()
def hello():
    click.echo('Hello! My name is Jeremiah Canty and im learning about dockers!')

if __name__ == '__main__':
    hello()
