def create(filename, content):
    """Writes content to a file."""
    try:
        print(f'Creating file {filename} with {content if len(content) > 0 else "empty contents"}')
        with open(filename, "w") as open_file:
            open_file.write(content)
    except Exception as e:
        print(f"Error creating file: {e}")
        raise e
    print(f"File {filename} created successfully")


def copy_file(source, destination):
    """Copies a file from location to another."""
    try:
        print(f"Copying file {source} to {destination}")
        with open(source, "r") as source_file:
            source_content = source_file.read()
            with open(destination, "w") as destination_file:
                destination_file.write(source_content)
    except Exception as e:
        print(f"Error copying file: {e}")
        raise e
    print(f"File {destination} copied successfully")


def merge_files(source_one, source_two, destination):
    """Combines two files and puts into one."""
    print(f"Combining file {source_one} and {source_two} to {destination}")
    try:
        with open(source_one, "r") as source_file:
            source_one_data = source_file.read()
    except Exception as e:
        print(f"Error copying {source_one}: {e}")
        raise e
    try:
        with open(source_two, "r") as source_file:
            source_two_data = source_file.read()
    except Exception as e:
        print(f"Error copying {source_two}: {e}")
        raise e
    try:
        with open(destination, "w") as destination_file:
            destination_file.write(source_one_data + source_two_data)
    except Exception as e:
        print(f"Error writing to {destination_file}: {e}")
        raise e
    print(f"File {destination} merged successfully")
