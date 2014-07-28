# batlog2csv

Convert [batlog][1] data files into comma separated files.

## Requirements

- A [Python][2] installation.
- A batlog data file (see `example.dat` for an example data file).

## Usage

Download the `batlog2csv.py` script and run it with the data file as its only argument, e.g.:

```bash
python batlog2csv.py batlog.dat
```

This will display the CSV in your terminal. You'll probably want to redirect the output to a file, e.g.:

```bash
python batlog2csv.py batlog.dat > batlog.csv
```

[1]: https://github.com/jradavenport/batlog
[2]: https://www.python.org/download/