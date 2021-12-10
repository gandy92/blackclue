# BlackClue
BlackClue is a python tool and package to extract GPS and acceleration data from 
BlackVue MP4 recordings. 
It is based on the excellent [pymp4](https://github.com/beardypig/pymp4).
While developed and tested with a BlackVue DR750S-1CH it should work with other 
models of that brand.

# License
BlackClue is licensed unter the [Apache 2.0 License](LICENSE). 

# Installation
BlackClue can be installed from the [Python Package Index](https://pypi.org/):
```bash
python3 -m pip install blackclue
```

# Usage
Used as a command line tool, BlackClue provides the following functionality:
```bash
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

Leave bug reports and feature requests on https://github.com/gandy92/blackclue.

# History
## 1.1.1
Fix problems with PyPI release.

## 1.1.0
First release on PyPI. Thanks to [Bart Broere](https://github.com/bartbroere), 
BlackClue can now also be used as a package.

## 1.0.0
First release on GitHub
