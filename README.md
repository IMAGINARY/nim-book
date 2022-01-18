# nim-book

A book that plays the game of Nim (very well).

This repository builds the book.

## Installing

- Install poetry

- Install dependencies by running

```
poetry install
```

## Building

The build process uses the `invoke` task runner, which is installed as a dependency. 

Run

```
poetry run invoke build
```

### Other tasks

There are other tasks you can `invoke`:

- `build-state-images`: Builds the SVG files that represent game states
- `build-html`: Builds the HTML file
- `build-pdf`: Converts the HTML (plus SVG) to a PDF file
- `clean`: Deletes output SVG, HTML and PDF file
