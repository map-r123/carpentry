# carpentry
A script to help with the creation of a cutting list

# Carpentry Cutting List Generator

A Python tool for generating cutting lists for kitchen cabinets. Define your cabinets by type and length, and the tool calculates all the individual panel dimensions needed (sides, bottoms, tops, doors, shelves, etc.) and exports them to an Excel spreadsheet ready for the workshop.

Available as both a command-line script and a GUI application.

## Features

- Supports two cabinet types:
  - **Bottom/Base cabinets** — standard base units
  - **Wall cabinets** — upper units, with shelf quantity automatically scaled to cabinet height
- Automatically calculates panel dimensions (length, width, edge banding, grooves, ports) for:
  - Bottom and top panels
  - Side panels
  - Cleats
  - Backstrips
  - Doors (single or double, based on cabinet width)
  - Masonite (back panel)
  - Shelves
- Aggregates identical parts across all cabinets in a project into a single summarized cutting list
- Exports the final list to a `.xlsx` file via [openpyxl](https://openpyxl.readthedocs.io/)
- Simple `tkinter`-based GUI for building a project visually before export

## Requirements

- Python 3.10+
- [openpyxl](https://pypi.org/project/openpyxl/)

Install dependencies:
```bash
pip install openpyxl
```

`tkinter` is required for the GUI and ships with most standard Python installations

## Usage

### Command line (`carpent.py`)

Run the script directly:
```bash
python carpent.py
```

You'll be prompted for:
1. The total number of cabinets in the project
2. For each cabinet: its type (`B` for a base cabinet, `W` for a wall cabinet) and its length in mm

Once complete, a `project.xlsx` file is generated in the current directory containing the full cutting list.

### GUI (`carpent_gui.py`)

Run the GUI:
```bash
python carpent_gui.py
```

1. Select a cabinet **type** from the dropdown (`Bottom` or `Wall`)
2. Enter a **length** in mm (must be greater than 99mm)
3. Click **Add** to add it to the project — it will appear in the list
4. Select a row and click **Remove** to remove a cabinet from the project
5. Click **Create Excel** to name the project and export the cutting list to a `.xlsx` file

## Output format

The generated spreadsheet contains one row per unique part

Identical parts (same name, dimensions, and options) from different cabinets are automatically combined into a single row with a summed quantity.

## Project structure

```
.
├── carpent.py       # Core logic: Cabinet/Wall classes, part calculations, Excel export
├── carpent_gui.py    # Tkinter GUI front-end, built on top of carpent.py
└── README.md
```

## Planned improvements

- Differnt types of unit support (conner units(top/bottom), wardrobes, etc)
- Beauty panel support

## License

No license specified.