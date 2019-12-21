import glob
import os
import shutil
from datetime import datetime
from PIL.ExifTags import TAGS
from PIL import Image

photo_from = "D:\!PHONE TEMP\!DEV_FOLDER"               #       The directory from which images are scanned
photo_to = "D:\!PHONE TEMP\!DEV_FOLDER_CONVERTED"       #       The directory to which the images will be sorted
DateTimeOriginal = 36867                                #       Tag ID for exif original date and time
dev = False                                             #       development mode


#       Function that returns the date & time of a given photo
def getDate(path):
    if path.endswith(".jpg"):
        exif_date = Image.open(path)._getexif()[DateTimeOriginal]
        date = exif_date[:10]
    elif path.endswith(".mp4"):
        mdate = os.path.getmtime(path)
        date = datetime.fromtimestamp(mdate).strftime('%Y-%m-%d')
        print(date)
    return date

#       Loops through every file in the source foldr
for path in glob.glob(photo_from+'/*'):
    f_date = getDate(path)
    year = f_date[:4]
    month = f_date[5:7]

    print("Y = ", year, " M = ", month)
    destination = photo_to + "\\" + year + "\\" + month

#       If the path doesnt exist, create it
    if not os.path.exists(destination):
        os.makedirs(destination)
        print("**** CREATED DIR ", destination, " ****")

#       Copy the file to the sorted destination
    shutil.copy2(path, destination)
    print(path, " MOVED TO ", destination)
    