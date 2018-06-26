# BlackClue
A Python Tool to extract GPS and Acceleration data from BlackVue MP4 recordings.
Leave bug reports and feature requests on https://github.com/gandy92/blackclue.

# License
BlackClue is licensed unter the [Apache 2.0 License](LICENSE). 

# Usage

`blackclue` is based on the excellent [pymp4](https://github.com/beardypig/pymp4).
It was developed and tested with a BlackVue DR750S-1CH but should work with other 
models of that brand.


```
$ blackclue -h
Usage: blackclue [OPTIONS] filelist

  Extract GPS and Acceleration data from BlackVue MP4 recordings.

  BlackVue extracts data embedded in the MP4 recordings of a BlackVue
  Dashcam.

Options:
  -c, --dump-embedded    Dump complete embedded data.
  -r, --dump-raw-blocks  Dump raw blocks from embedded data.
  -x, --extended-scan    Do not stop scanning file after processing the
                         embedded data.
  -v, --verbose          Print some additional information.
  -h, --help             Show this message and exit.
```
