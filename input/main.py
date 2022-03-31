#!/usr/bin/env python
import os
import xarray as xr
import pandas as pd
import pickle
import os

def process_dataset(fi):
    print("reading dataset...")
    ds = xr.open_dataset(os.path.join("/input", fi), engine='pynio')
    print("converting to pandas dataframe...")
    df = ds.to_dataframe()
    print("saving to pickle file.")
    new_fi = "%s.pickle" % os.path.basename(fi)
    df.to_pickle(os.path.join("/output", new_fi))
    print("done")

# we could easily walk this for multiple inputs..
if __name__ == "__main__":
    process_dataset("/input/rotations.grib2")
