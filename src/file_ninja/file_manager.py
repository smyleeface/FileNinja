def create(filename, content):
    """Writes content to a file."""
    try:
        print(
            f'Creating file {filename} with {content if len(content) > 0 else "empty contents"}'
        )
        with open(filename, "w") as open_file:
            open_file.write(content)
    except Exception as e:
        print(f"Error creating file: {e}")
        raise e
    print(f"File {filename} created successfully")
