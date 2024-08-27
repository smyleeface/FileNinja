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


if __name__ == "__main__":
    cli.add_command(create_file)
    cli()
