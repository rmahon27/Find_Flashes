import numpy as np 
from matplotlib import pyplot as plt
from astropy.io import fits
import glob


file_path = input("Enter File Path: \n")

print()

file_format = input("Enter Format of .fits files: \n")

print()

image_num_list = []

time_stamp_list = []

image_num = 1 
for file in glob.glob(file_path+ "\\" + file_format + "*.fits"):
    image_full = fits.open(file)
    image = image_full[0].data

    header = image_full[0].header

    file_time = header["DATE-AVG"][11:]

    row_num = image.shape[0]
    col_num = image.shape[1]
    flash_count = 0 
    
    col_means = []
    for col in range(col_num):
        current_column = image[:,col]
        col_mean = np.mean(current_column)
        col_means.append(col_mean)

    avg_mean = np.mean(col_means)
    for elem in range(len(col_means)):
        mean_elem = col_means[elem]
        ratio = avg_mean/mean_elem
        
        if ratio < 0.1:
            flash_count += 1 
    
    if flash_count >5: 
        image_num_list.append(image_num)
        time_stamp_list.append(file_time)
        
    image_num += 1 

print("Flash appears in following image numbers: \n")
for i in range(len(image_num_list)):
    print("Image Number: {}    Time Stamp: {}".format(image_num_list[i], time_stamp_list[i]))
        