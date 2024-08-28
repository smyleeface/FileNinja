# File Ninja

## Description

This is a simple file manager that allows you to:

* Create a file (empty or with optional text)
* Copy a file
* Combine two files into a third
* Delete a file

## Development
 
* Python 3.11

From the root of the project, install the package in editable mode:

```bash
pip install -e .
```

To see commands available in the application:

```bash
python src/file_ninja/main.py
```

Add `--help` to any command to get usage information:

```bash
python src/file_ninja/main.py create-file --help
```

## Testing

```bash
python -m unittest discover -s tests/file_ninja -p '*_test.py'
```

## Building

```bash
pip install .[build]
pyinstaller src/file_ninja/main.py -n fini
cd dist/fini/
./fini
```

* Docker (building for other platforms)

```
docker run --rm -it -v $(pwd):/app -w /app python:3.11 bash
pip install .[build]
pyinstaller src/file_ninja/main.py -n fini
cd dist/fini/
./fini
```
