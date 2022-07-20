# Spectral Indices Analysis using geospatial frameworks

This repository contains some python scripts using geemap and earth engine api for analysis of various spectral indices over a given time frame.

## Various Spectral Indices 
We have implemented the following indices and included the code snippets for the following:

NDVI

** A short laymen description about NVDI.. Add proper links and goto materials

NDBI

** A short laymen description about NDWI

MNDWI

** A short laymen description about MNDWI

## Library Installations

1. Sign up in the Google Earth Engine.
2.

It is always advised to create a conda environment to install all the earth engine related dependencies.

,,,

,,,

## Example Unit Tests
*A beginners guide*

Several *Unit Test* scripts are also available for future experiments. All the unit tests are provided in the notebook (.ipynb) format and can be directly executed at the users end using jupyter notebook.

This will also serve as a guide for people who are just getting started working with earth engine and geemap and want to understand and explore this work. This code snippets are tests done before compiling the final workflow.


1. [Downloading a range of images (by date)](unit-tests-notebooks/downloading-a-range-of-images-by-date.ipynb)
2. [Clipping the Image Collection to the shapefile](unit-tests-notebooks/clipping-an-image-collection-to-the-shapefile.ipynb)
3. Download 2001 data season wise
4. Check the seasonal and annual mean image 
5. Check NDVI index in the year 2001
6. Download a computed image in a self set palette
7. [Converting a GEOtiff file to a labelled map in any format](unit-tests-notebooks/converting-a-GEOtiff-file-to-a-labelled-map-in-any-format.ipynb)


### Final Executable Scripts

For now notebooks are created for interactive visualization.

1. Run the [custom-parameter-initialization](final_scripts/custom-parameter-initialization.ipynb) notebook. Here the name of the target districts, years of computation, etc can be custom initialized.
2. Run the [ndvi-computation-and-GEOtiff-file-create](final_scripts/ndvi-computation-and-GEOtiff-file-create.ipynb) notebook,which will compute the specified spectral indices (ndvi in this case) and generate GEOtiff files for the same.
3. Run the final notebook, [converting-a-GEOtiff-file-to-a-labelled-map-in-any-format](final_scripts/converting-a-GEOtiff-file-to-a-labelled-map-in-any-format.ipynb), which will generate maps for a given GEOTiff file.