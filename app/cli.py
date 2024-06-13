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


@cli.command()
def add_credential():
    if user_id is None:
        click.echo('Please login first.')
        return
    website = input('Enter website: ')
    username = input('Enter username: ')
    password = input('Enter password: ')
    category = input('Enter category (optional): ')
    credentials.add_credential(user_id, website, username, password, category)
    click.echo('Credential added.')

@cli.command()
def retrieve_credential():
    if user_id is None:
        click.echo('Please login first.')
        return
    website = input('Enter website: ')
    credential = credentials.get_credential(user_id, website)
    if credential:
        click.echo(f'Website: {credential.website}')
        click.echo(f'Username: {credential.username}')
        click.echo(f'Password: {credential.password}')
        click.echo(f'Category: {credential.category}')
    else:
        click.echo('Credential not found.')

@cli.command()
def update_credential():
    if user_id is None:
        click.echo('Please login first.')
        return
    website = input('Enter website: ')
    username = input('Enter new username: ')
    password = input('Enter new password: ')
    category = input('Enter new category (optional): ')
    credentials.update_credential(user_id, website, username, password, category)
    click.echo('Credential updated.')

@cli.command()
def delete_credential():
    if user_id is None:
        click.echo('Please login first.')
        return
    website = input('Enter website: ')
    credentials.delete_credential(user_id, website)
    click.echo('Credential deleted.')

@cli.command()
def list_credentials():
    if user_id is None:
        click.echo('Please login first.')
        return
    creds = credentials.list_credentials(user_id)
    for cred in creds:
        click.echo(f'Website: {cred.website}')
        click.echo(f'Username: {cred.username}')
        click.echo(f'Password: {cred.password}')
        click.echo(f'Category: {cred.category}')
        click.echo('-'*20)

if __name__ == '__main__':
    cli()