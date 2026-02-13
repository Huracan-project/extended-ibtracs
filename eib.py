import huracanpy

# Calc
import numpy as np
import pandas as pd
import xarray as xr
from haversine import haversine
import geopandas as gpd

# Interface
from tqdm import tqdm
from glob import glob
import os
import pickle as pkl

# Plots
import matplotlib.pyplot as plt
import seaborn as sns
import cartopy.crs as ccrs
from shapely.geometry import Polygon, MultiPolygon, Point

# Parameters
BASINS = ["NA", "EP", "NI", "SA", "SI", "SP", "WP"]

cmap = sns.color_palette("tab20").as_hex()
PALETTE = {
    'IBTrACS':"black", 
    'TRACK-ERA5':cmap[0], # Dark blue
    'SyCLoPS-ERA5':cmap[1], # Light blue
    'TRACK-JRA3Q':cmap[2], # Dark orange
    'SyCLoPS-JRA3Q':cmap[3], # Light orange
    'TRACK-MERRA2':cmap[4], #Dark green
    'SyCLoPS-MERRA2':cmap[5], # Light green,
    'TRACK-ECMWF-OP-AN':cmap[6], # Violet
    'TRACK-NCEP':cmap[8], # Brown
}
SOURCES = list(PALETTE.keys())