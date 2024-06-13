import click
from .auth import Auth
from .credentials import Credentials

auth = Auth()
credentials = Credentials()
user_id = None

@click.group()
def cli():
    pass

@cli.command()
def register():
    username = input('Enter username: ')
    password = input('Enter password: ')
    if auth.register(username, password):
        click.echo('Registration successful.')
    else:
        click.echo('Username already exists.')

@cli.command()
def login():
    global user_id
    username = input('Enter username: ')
    password = input('Enter password: ')
    user_id = auth.login(username, password)
    if user_id:
        click.echo('Login successful.')
    else:
        click.echo('Invalid credentials.')

if __name__ == '__main__':
    cli()