import click

import file_ninja.file_manager as file_manager


@click.group()
def cli():
    pass


@click.command()
@click.option(
    "--filename",
    prompt="Name of file",
    default="new_file",
    help="Name of the file to create.",
)
@click.option(
    "--content",
    prompt="Enter any content for the file, or leave blank",
    default="",
    help="Content to write to the file.",
)
def create_file(filename, content):
    file_manager.create(filename, content)


@click.command()
@click.option(
    "--source",
    prompt="File to copy",
    required=True,
    help="Name of the file to copy",
)
@click.option(
    "--destination",
    prompt="Copy location",
    required=True,
    help="Where to copy file to",
)
def copy_file(source, destination):
    file_manager.copy_file(source, destination)


if __name__ == "__main__":
    cli.add_command(create_file)
    cli.add_command(copy_file)
    cli()
