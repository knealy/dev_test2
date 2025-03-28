# Character Grid Generator

A Python script that generates a character grid from a Google Docs document containing coordinate-based character positions.

## Description

This script fetches content from a Google Docs document and processes it to create a visual grid of characters based on coordinate pairs. It's particularly useful for visualizing text-based art or coordinate-based character arrangements.

## Features

- Fetches content from Google Docs documents
- Parses coordinate-based character positions (x,y) with associated characters
- Generates a visual grid representation
- Handles multi-digit x-coordinates
- Filters out invalid characters (ASCII control characters)

## Requirements

- Python 3.x
- `requests` library
- `beautifulsoup4` library

## Installation

1. Clone this repository
2. Install the required dependencies:
```bash
pip install requests beautifulsoup4
```

## Usage

```python
from character_grid import create_character_grid

# Create a grid from a Google Docs URL
url = 'your_google_docs_url'
grid = create_character_grid(url)
```

## Input Format

The script expects the Google Docs document to contain coordinate pairs in the following format:
- `xychar` where:
  - `x` is a one or two-digit number (x-coordinate)
  - `y` is a single digit number (y-coordinate)
  - `char` is the character to place at that position

Example:
```
1@0 2#1 3$2
```

## Output

The script will print the generated grid to the console, with characters positioned according to their coordinates. Empty spaces are represented by spaces, and only non-empty rows are displayed.

## Example

```python
url = 'https://docs.google.com/document/d/e/2PACX-1vRMx5YQlZNa3ra8dYYxmv-QIQ3YJe8tbI3kqcuC7lQiZm-CSEznKfN_HYNSpoXcZIV3Y_O3YoUB1ecq/pub'
character_grid = create_character_grid(url)
```

## Notes

- The script only processes valid Unicode characters (ASCII control characters are filtered out)
- Empty rows are not displayed in the output
- The grid is created based on the maximum x and y coordinates found in the input 