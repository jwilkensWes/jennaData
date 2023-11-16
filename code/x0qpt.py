## x0qpt.py
## Testing file for python scripts in qgis 

## Set Up Statements
import ee
# ee.Initialize()
from ee_plugin import Map


## Collection Parameters
# landsat surface reflectance data
l8sr = ee.ImageCollection('LANDSAT/LC08/C02/T1_L2') ## land 8
# bands needed for indexs
l8bands = ['SR_B5', 'SR_B4', 'SR_B6', 'SR_B3']
# random points in fire areas
pts = ee.FeatureCollection('projects/poulos-gee/assets/fire_ign')
# the first point in dataset
ptx = ee.Feature(pts.first())

# buffer
def buf(col):
    pt = ee.Feature(col).buffer(15)
    return(pt)

# zonal stats
def zonal_ndvi(col):
    ign = col.get('ignitiondate')
    mon3 = col.get('prior3m_ign')
    img = l8ndvi.filterDate(mon3, ign)
    
    def zone(imgcol):
        reg = imgcol.reduceRegions(
                reducer = ee.Reducer.mean(),
                collection = col,
                scale = 30)
        return reg
    
    zstat = img.map(zone)
    return zstat



## Add Desired Layers to Map
Map.addLayer(pt)

"""
def make_ndvi_lan8(image):
    nir = image.select('SR_B5')
    red = image.select('SR_B4')
    ndvi = nir.subtract(red).divide(nir.add(red)).rename('NDVI')
    return ndvi
def cloud_mask_lan8(img):
    cloud_mask = img.select('QA_PIXEL').bitwiseAnd(ee.Number.parse('0000001111', 2)).eq(0)
    return(img.select(l8bands).updateMask(cloud_mask))

# filter 
l8sr = l8sr.filterBounds(interestArea)
l8sr = l8sr.filterDate(startDate8, endDate8)
l8sr = l8sr.filter(ee.Filter.calendarRange(7, 10, 'month'))
l8cloud = l8sr.map(cloud_mask_lan8)

cday = ee.Date('2013-08-31')
cloudy = l8sr.filterDate(cday, cday.advance(1, 'day'))
"""



"""
## Collection Parameters

# start and end dates for each satilite
# landsat 8
startDate8 = ('2013-07-01')
endDate8 = ('2022-10-01')
# landsat 7
startDate7 = ('2008-07-01')
endDate7 = ('2012-10-01')



# landsat surface reflectance data
l8sr = ee.ImageCollection('LANDSAT/LC08/C02/T1_L2') ## land 8
l7sr = ee.ImageCollection('LANDSAT/LE07/C02/T1_L2') ## Land 7

# area to be collected
interestArea = ee.FeatureCollection('projects/poulos-gee/assets/Stanislaus_Area_Polygon').geometry()
# polygons for zonal stats
treatments = ee.FeatureCollection('projects/poulos-gee/assets/Variable_Density_Study_Polygon')
# bands needed for indexs
l8bands = ['SR_B5', 'SR_B4', 'SR_B6', 'SR_B3']
l7bands = ['SR_B4', 'SR_B3', 'SR_B2', 'SR_B5']


l7sr = l7sr.filterBounds(interestArea)
l7sr = l7sr.filterDate(startDate7, endDate7)
l7sr = l7sr.filter(ee.Filter.calendarRange(7, 10, 'month'))

l7sr.first().getInfo()
Map.addLayer(l7sr.first())
"""

"""
startDate = ('2019-07-01')
endDate = ('2019-10-01')
startDate7 = ('2011-07-01')
endDate7 = ('2011-10-01')
interestArea = ee.FeatureCollection('projects/poulos-gee/assets/Stanislaus_Area_Polygon').geometry()
l8bands = ['SR_B5', 'SR_B4', 'SR_B6', 'SR_B3']
l7bands = ['SR_B4', 'SR_B3', 'SR_B2', 'SR_B5']
# data import statements
l8col = ee.ImageCollection('LANDSAT/LC08/C02/T1_L2')
l8col = l8col.filterDate(startDate, endDate)
l8col = l8col.filterBounds(interestArea) 
l7col = ee.ImageCollection('LANDSAT/LE07/C02/T1_L2')
l7col = l7col.filterDate(startDate7, endDate7)
l7col = l7col.filterBounds(interestArea) 
treatments = ee.FeatureCollection('projects/poulos-gee/assets/Variable_Density_Study_Polygon')

treatments = treatments
    
def clip_to_area(image):
    clipped = image.clip(interestArea)
    return clipped
def make_ndvi_lan8(image):
    nir = image.select('SR_B5')
    red = image.select('SR_B4')
    ndvi = nir.subtract(red).divide(nir.add(red)).rename('NDVI')
    return ndvi
def make_ndvi_lan7(image):
    nir = image.select('SR_B4')
    red = image.select('SR_B3')
    ndvi = nir.subtract(red).divide(nir.add(red)).rename('NDVI')
    return ndvi


def cloud_mask_lan8(img):
    cloud_mask = img.select('QA_PIXEL').bitwiseAnd(ee.Number.parse('0000001111', 2)).eq(0)
    return(img.select(l8bands).updateMask(cloud_mask))
def cloud_mask_lan7(img):
    cloud_mask = img.select('QA_PIXEL').bitwiseAnd(ee.Number.parse('0000001111', 2)).eq(0)
    return(img.select(l7bands).updateMask(cloud_mask))
# l8clip = l8col.map(clip
# l8clip = l8col.map(clip_to_area)
# l8ndvi = l8col.map(make_ndvi_lan82)
# qa = l8ndvi.first()
# qa = qa.clip(interestArea)
cloud8 = l8col.map(cloud_mask_lan8)
cloud7 = l7col.map(cloud_mask_lan7)
# qa = cloud.map(make_ndvi_lan8)
# qa = qa.first()
cloud8 = cloud8.first()
cloud7 = cloud7.first()

nomask = l8col.first()
# add qa to map
Map.addLayer(treatments)

# task = ee.batch.Export.image.toDrive(image = qa)
# task.start()

## missing parse function
# ef list_interest_images(image):
"""    
    
