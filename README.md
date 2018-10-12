# BlackClue
A Python tool to extract GPS and Acceleration data from BlackVue MP4 recordings. 
It can also be used as a package.

# License
BlackClue is licensed unter the [Apache 2.0 License](LICENSE). 

# Installation
While not available via PyPI, blackvue can be installed manually:
```bash
$ git clone https://github.com/gandy92/blackclue.git
$ sudo python3 -m pip install -e .
```

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

Leave bug reports and feature requests on https://github.com/gandy92/blackclue.

# History
## 1.1.0
First release on PyPi. Thanks to @bartbroere, BlackClue can now also be used as a package.

## 1.0.0
First release on GitHub

# Todo
Make it available on [PyPI](https://pypi.org/) to be installed via pip.
