import sys
import click

import utils


sys.path.insert(1, './forgepb')


@click.command(
    'tags',
    help='List '
)
def list_tags_cmd():
    release_versions = utils.get_versions()
    [print(version) for version in release_versions[::-1]]
    return


@click.command(
    'branches',
    help='List provenance brances that can be checked out to'
)
def list_branches_cmd():
    branches = utils.get_remote_branches()
    [print(branch) for branch in branches]
    return