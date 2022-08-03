# Imports
# from hashlib import _BlakeHash
import os
import geemap
import geemap.colormaps as cm
import ee
import warnings

from helpers import yearlyMap

# from helpers import clip_to_shape
warnings.filterwarnings('ignore')

# State the start and end year of evaluation
start_year = 2000
end_year = 2002

# List the districts you want to evaluate
districts = ['Bangalore Urban', 'Jorhat','Cachar']

# Python dictionary where the 'key' states the yearly timeframes to be evaluated
# mam: mar-apr-may; jjas: jun-jul-aug-sep; on: oct-nov; djf: dec-jan-feb; ann: annual
# The values indicates the stating and the ending dates of the timesframes to be evaluated
# [start date, start month, end date, end month]
seasons = {'mam': [1, 3, 31, 5], 'jjas': [1, 6, 30, 9], 'on': [
    1, 10, 30, 11], 'djf': [1, 12, 28, 2], 'ann': [1, 3, 28, 2]}



def main():

    ee.Initialize()
    # authenticate earth engine
    # one may save the token locally to make this step easier
    # ee.Authenticate()

    # Get the district shapefile dataset from Google Earth Engine
    dataset = ee.FeatureCollection("FAO/GAUL/2015/level2")

    # The landsat 7 data is called from the Google Earth Engine Server and a Image Collection is created.
    dataset_l7 = ee.ImageCollection('LANDSAT/LE07/C01/T1_RT_TOA')

    # Loop over the shapefiles and store them as feature collection.
    shape_collection = []
    for district in districts:
        roi = dataset.filter(ee.Filter.eq('ADM2_NAME', district))
        shape_collection.append(roi)

    # A python dictionary where key is the shapefile feature collection and corresponding value is the name of the district.
    shape_files = dict(zip(shape_collection, districts))

    # List of years
    years = [y for y in range(start_year,end_year)]

    for roi, district_name in shape_files.items():
        # Loop the computation over the specified list of years for this roi
        for year in years:
            yearlyMap(dataset_l7,seasons, year,district_name,roi)

if __name__ == "__main__":
    main()