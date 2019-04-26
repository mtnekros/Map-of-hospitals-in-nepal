import arcpy
from arcpy import env
from arcpy.sa import *


# set environment settings
env.workspace = r"C:\Users\Diwas Tamang\Desktop\Studies\Python\Project\FoliumPractise\Data"

# set local variables
inRaster = "dem"
outMeasurement = "DEGREE"
zFactor = 1

# execute slope
outSlope = Slope(inRaster, outMeasurement, zFactor)

# save the output
outSlope.save(r"C:\Users\Diwas Tamang\Desktop\Studies\Python\Project\FoliumPractise\Data\outSlope")
