# nim-book

A book that plays the game of Nim (very well).

This repository builds the book.

## Installing

- Ideally create a virtual environment (virtualenv) with python 3.7

- Activate the new virtual environment

- Install the dependencies by running

```
pip install -r requirements.txt
```

## Building

The build process uses the `invoke` task runner, which is installed as a dependency. 

Run

```
invoke build
```

(assuming `invoke` is in your path. It'll be installed in the `bin` directory of your virtual env).

### Other tasks

There are other tasks you can `invoke`:

- `build_state_images`: Builds the SVG files that represent game states
- `build_html`: Builds the HTML file
- `build_pdf`: Converts the HTML (plus SVG) to a PDF file
- `clean`: Deletes output SVG, HTML and PDF file
