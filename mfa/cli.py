""":mod:`mfa.cli` --- Command-line interface
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""
import click
import keyring
import onetimepass


@click.group()
def cli():
    """Multi-factor authentication on your command line."""
    pass


@cli.command()
@click.argument('key')
@click.argument('value')
@click.option('--force', is_flag=True)
def set(key, value, force):
    """Set a value for a key."""
    if keyring.get_password(__name__, key) and not force:
        click.echo("Use '--force' to overwrite existing key.")
    else:
        keyring.set_password(__name__, key, value)


@cli.command()
@click.argument('key')
def get(key):
    """Get the value for the key."""
    click.echo(keyring.get_password(__name__, key))


@cli.command()
@click.argument('key')
def delete(key):
    """Delete the key."""
    try:
        keyring.delete_password(__name__, key)
    except Exception as e:
        click.echo((Exception, e))


@cli.command()
@click.argument('key')
def otp(key):
    """Generate a one-time password using TOTP."""
    password = keyring.get_password(__name__, key)
    try:
        totp = onetimepass.get_totp(password, as_string=True)
    except Exception as e:
        click.echo(e)
    else:
        click.echo(totp)
