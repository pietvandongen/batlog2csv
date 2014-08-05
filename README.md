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

## Example

This input:

```
Tue Aug 14 10:41:46 PDT 2012
    | |           "DesignCycleCount70" = 65535
    | |           "CycleCount" = 1
    | |           "DesignCycleCount9C" = 1000
    | |           "MaxCapacity" = 6667
    | |           "CurrentCapacity" = 6329
    | |           "LegacyBatteryInfo" = {"Amperage"=18446744073709550808,"Flags"=4,"Capacity"=6667,"Current"=6329,"Voltage"=8207,"Cycle Count"=1}
    | |           "DesignCapacity" = 6700
Tue Aug 14 10:43:00 PDT 2012
    | |           "DesignCycleCount70" = 65535
    | |           "CycleCount" = 1
    | |           "DesignCycleCount9C" = 1000
    | |           "MaxCapacity" = 6667
    | |           "CurrentCapacity" = 6308
    | |           "LegacyBatteryInfo" = {"Amperage"=18446744073709550810,"Flags"=4,"Capacity"=6667,"Current"=6308,"Voltage"=8204,"Cycle Count"=1}
    | |           "DesignCapacity" = 6700
```

Will convert to this:

```csv
Date,CycleCount,MaxCapacity,CurrentCapacity,DesignCapacity
2012-08-14 10:41:46,1,6667,6329,6700
2012-08-14 10:43:00,1,6667,6308,6700
```

## License

Apache License, Version 2.0, see `LICENSE.md`.

[1]: https://github.com/jradavenport/batlog
[2]: https://www.python.org/download/