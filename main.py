import getopt
import re
import sys

import geopandas as gpd
import pandas as pd
from shapely import Polygon


def readfile(file):
    filedata = pd.read_csv(file)
    filedata.drop(columns=['Lower Altitude', 'Lat Lon Neighbor'], inplace=True)
    filedata = (filedata
                .rename(columns={"Facility ID": "artcc", "Upper Altitude": "altitude",
                                 "Latitude": "latitude", "Longitude": "longitude"}))
    filedata['latitude'] = filedata['latitude'].apply(dms2dd)
    filedata['longitude'] = filedata['longitude'].apply(dms2dd)
    filedata.dropna(axis=0, inplace=True)
    gdf = gpd.GeoDataFrame(
        filedata, geometry=gpd.points_from_xy(filedata.longitude, filedata.latitude), crs="EPSG:4326"
    )
    return gdf


def dms2dd(dms: str):
    if not isinstance(dms, str):
        return float('NaN')

    pattern = r"(\d{3})(\d{2})(\d{2})(\d{2})([N,S,E,W]{1})" if (len(dms) == 10) \
        else r"(\d{2})(\d{2})(\d{2})(\d{2})([N,S,E,W]{1})"
    results = re.fullmatch(pattern, dms)
    if results is None:
        return float('NaN')
    degrees, minutes, seconds, decisecond, direction = re.search(pattern, dms).groups()
    dd = float(degrees) + float(minutes)/60 + (float(seconds) + float(decisecond)*.01) /(60*60)
    if direction in ('S', 'W'):
        dd *= -1
    return dd


def main(argv):
    inputfile = ''
    opts, args = getopt.getopt(argv, "hi:", ["ifile="])
    for opt, arg in opts:
        if opt == '-h':
            print('test.py -i <inputfile>')
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
    print('Input file is ', inputfile)

    artccs = readfile(inputfile)
    artccs = (artccs.groupby(artccs.artcc)['geometry']
              .apply(lambda x: Polygon(x.tolist())))
    artccs.crs = 'epsg:4326'
    print(type(artccs))
    artccs.to_file('artccs.shp', driver='ESRI Shapefile')


if __name__ == "__main__":
    main(sys.argv[1:])
