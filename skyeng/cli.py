from argparse import ArgumentParser

import toml

from .session import Session
from .commands import COMMANDS


parser = ArgumentParser(prog='skyeng')
parser.add_argument('-c', '--config', default='./config.toml')
parser.add_argument('command', choices=COMMANDS.keys())


def cli(args):
    parsed, unknown = parser.parse_known_args(args)
    config = toml.load(parsed.config)
    session = Session()
    session.auth(
        email=config['credentials']['email'],
        password=config['credentials']['password'],
    )
    user = session.get_user()
    command = COMMANDS[parsed.command]
    return command(user, unknown)
