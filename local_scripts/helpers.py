import ee
import os
import geemap
import geemap.colormaps as cm


def clip_to_shape(roi):
    '''
    Function to take an image and clip it according to the region of interest(roi).
    It takes an image as an input and outputs the clipped version of the image according to roi
    '''
    def _clip(image):
        return image.clip(roi)
    return _clip


def maskclouds(image):
    '''
    Function to take an image and mask the clouds for better visibility. The returns the masked image.
    '''
    # Select the BQA band, which has the cloud information
    qa = image.select('BQA')

    # In BQA Band bit 4 is the cloud band, hence activate only that bit, set all other bits of BQA to zero
    cloudBit = 1 << 4 #(00000001 -> 00010000) 

    # Both flags should be set to zero, indicating clear conditions.
    mask = qa.bitwiseAnd(cloudBit).eq(0) # And with all the other bits of BQA to check for clouds
    return image.updateMask(mask)

def ndvi_image_compute(img):
    '''
    Function to compute the ndvi index of the averaged image.It also initializes a download ready ndvi pallete for
    visualization and returns the final color image (with pallete)/.
    '''
    # Computes the nvdi index of the image which is (Band 4 – Band 3) / (Band 4 + Band 3) for LandSAT 7.
    ndvi_img = img.normalizedDifference(['B4', 'B3'])
    ndvi_visualization = {
#       'min': -0.22789797020331423,
#       'max': 0.3912415762453296,
#       'palette': 'FFFFFF, CE7E45, DF923D, F1B555, FCD163, 99B718, 74A901, 66A000, 529400,' + \
#         '3E8601, 207401, 056201, 004C00, 023B01, 012E01, 011D01, 011301'
      'palette': cm.palettes.ndvi,
        }
    # Get a corrected image with the pallete specified.
    corrected_img = ndvi_img.visualize(**ndvi_visualization)
    
    return corrected_img

def filter_date(seasons,year,i,flag): # TODO: add function args for seasons
    '''
    Function to compute the start and the end date of a particular season. It takes the year and the season of 
    which we need to find the date and returns the start and the end date is YYYY/MM/DD format
    '''
    start_date = ee.Date.fromYMD(year,seasons[i][1],seasons[i][0])
    if flag==0:
        end_date = ee.Date.fromYMD(year,seasons[i][3],seasons[i][2])
    else:
        end_date = ee.Date.fromYMD(year+1,seasons[i][3],seasons[i][2])
    
    return start_date, end_date
    
def get_filtered_image(seasons,dataset_l7,year,i,roi,flag):
    # TODO: add an arg for dataset or implement inner function
    '''
    Function to get the final computed image of the year specified ( sort by filterdate_ cloud_masked + mean +
    ndvi computed)/. The function returns the final computed image.
    '''
    start_date,end_date = filter_date(seasons,year,i,flag)
    
    img = (dataset_l7.filterDate(start_date,end_date)
                    .filterBounds(roi)
                    .map(maskclouds)
                    .select('B3','B4')
                    .mean())
    img = ndvi_image_compute(img)
    return img



def download_to_drive(filename,year_folder,img,roi):
    '''
    Function to download the images year wise into the authenticated drive in a geotiff format in the specified
    year folders.
    '''
    task = ee.batch.Export.image.toDrive(image= img.clip(roi),
                                     description='ndvi index computation for two decades',
                                     scale=30,
                                     region=roi.geometry(),
                                     folder=year_folder,
                                     fileNamePrefix=filename,
                                     fileFormat='GeoTIFF')
    task.start()

def yearlyMap(dataset_l7,seasons,year,district_name,roi):
    '''
    Function to loop over the five selected intervals over an year by taking a year input.
    '''
    year_folder = district_name
    for k,season in enumerate(seasons):
        if season=='djf' or season== 'ann':
            img = get_filtered_image(seasons,dataset_l7,year,season,roi,flag=1) 
        else:
            img = get_filtered_image(seasons,dataset_l7, year,season,roi,flag=0)
        filename = season + '-' + str(year)
        download_to_drive(filename, year_folder,img,roi)

if __name__ == "__main__":
    pass