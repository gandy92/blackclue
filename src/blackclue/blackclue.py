#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from __future__ import print_function

import io
import logging
import os

import click
import clickutil
import construct
from pymp4.parser import Box

log = logging.getLogger(__name__)
construct.setglobalfullprinting(True)

# data offset, has_length, termination
emb_file_def = {
    b'sttm': (4, False, None, None),
    b'ptnm': (4, False, None, None),
    b'ptrh': (4, False, None, None),
    b'thum': (8, True,  None, '.jpg'),
    b'gps ': (4, False, b'\x00',  '.nmea'),
    b'3gf ': (4, False, b'\xff'*10, '.3gf'),
}


def dump(file, dump_embedded=False, dump_raw_blocks=False, extended_scan=False, verbose=False):
    """ Extract GPS and Acceleration data from BlackVue MP4 recordings.

    BlackVue extracts data embedded in the MP4 recordings of a BlackVue Dashcam.
    """
    for filename in file:
        filebase = os.path.splitext(filename)[0]
        with open(filename, 'rb') as fd:
            fd.seek(0, io.SEEK_END)
            eof = fd.tell()
            fd.seek(0)

            while fd.tell() < eof:
                try:
                    box = Box.parse_stream(fd)
                    # print(box)
                    content = dict(box.__getstate__())
                    ctype = content['type'].decode('utf8')
                    if 'data' in content and ctype == 'free':
                        offset = content['offset']
                        end = content['end']
                        data = content['data']
                        if verbose:
                            print("Found container of type '{}', data has length {}.".format(ctype, len(data)))
                        if dump_embedded:
                            with open(filename+"-{:012d}-{}.bin".format(offset, ctype),"wb") as ofd:
                                ofd.write(data)
                        idx = 0
                        while idx < len(data):
                            block_len = int.from_bytes(data[idx:idx+4], 'big')
                            block_data = data[idx+4:idx+block_len]
                            if verbose:
                                print("Found block with len {}".format(block_len))
                            if block_len == 0:
                                break
                            if dump_raw_blocks:
                                with open(filebase+"-{:012d}-{}-{:08d}.bin".format(offset, ctype, idx), "wb") as ofd:
                                    ofd.write(block_data)
                            if block_data[0:4] in emb_file_def:
                                first, has_length, termination, ext = emb_file_def[block_data[0:4]]

                                # some data like thmb indicates the length:
                                last = first + int.from_bytes(block_data[4:8], 'big') if has_length else block_len

                                # other data like gps is zero terminated:
                                last = block_data.find(termination) if termination is not None else last

                                if ext is not None:
                                    with open(filebase+ext, "wb") as ofd:
                                        ofd.write(block_data[first:last])

                                if ext == '.3gf':
                                    with open(filebase+ext+".txt", "wt") as ofd:
                                        n=0
                                        while first < last:
                                            chunk = block_data[first:first+10]
                                            time_ms = int.from_bytes(chunk[0:4], 'big')
                                            if time_ms == 0xffffffff:
                                                break
                                            acc_1u = int.from_bytes(chunk[4:6], 'big')
                                            acc_2u = int.from_bytes(chunk[6:8], 'big')
                                            acc_3u = int.from_bytes(chunk[8:10], 'big')
                                            acc_1s = int.from_bytes(chunk[4:6], 'big', signed=True)
                                            acc_2s = int.from_bytes(chunk[6:8], 'big', signed=True)
                                            acc_3s = int.from_bytes(chunk[8:10], 'big', signed=True)
                                            ofd.write(("{:8d} "+
                                                       "{:08x} {:04x} {:04x} {:04x} "+
                                                       "{:6d} {:6d} {:6d} {:6d}\n").format(
                                                n, time_ms, acc_1u, acc_2u, acc_3u, time_ms, acc_1s, acc_2s, acc_3s
                                            ))
                                            first += 10
                                            n += 1

                            idx += block_len
                        if verbose:
                            ("Got to idx {}.".format(idx))
                        if not extended_scan:
                            break

                except construct.core.ConstError:
                    break

                except Exception as e:
                    print(e)
                    raise


@click.command(context_settings=dict(help_option_names=['-h', '--help']))
@click.option('-c', '--dump-embedded', is_flag=True,
              help='Dump complete embedded data.')
@click.option('-r', '--dump-raw-blocks', is_flag=True,
              help='Dump raw blocks from embedded data.')
@click.option('-x', '--extended-scan', is_flag=True,
              help='Do not stop scanning file after processing the embedded data.')
@click.option('-v', '--verbose', is_flag=True,
              help='Print some additional information.')
@click.argument('FILE', nargs=-1, metavar='filelist')
@clickutil.call(dump)
def dump_cli():
    pass


if __name__ == '__main__':
    dump_cli()
