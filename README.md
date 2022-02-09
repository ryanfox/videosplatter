# Video splatter

Splat a video into a single image by sampling a frame at regular intervals. Useful
for seeing the changes over time of an entire video or movie.

Can produce "barcodes":
![barcode image from New York City aerial footage](city_barcode.jpg)

Or mosaics:
![mosaic image from New York City aerial footage](city_splat.jpg)
_Original from The Dronalist, used under CC-BY_

## Installation

```
pip install videosplatter
```

## Usage
Command line:
```
$ videosplatter <filename> [--start <start time in seconds>] [--end <end time in seconds>] [--interval <number of seconds between samples]
```

Example:

```
$ videosplatter city.mp4
```

Programmatic usage:
```
from videosplatter import splat

splat.splat(filename, start_time, end_time, interval)
```
