import numpy as np 
from matplotlib import pyplot as plt
from astropy.io import fits
import glob

Left_file_path = input("Enter File Path for Left Camera Images: \n")

print()

Right_file_path = input("Enter File Path for Right Camera Images: \n")

print()

Left_file_format = input("Enter Format for the Left Cam .fits files: \n")

print()

Right_file_format = input("Enter Format for the Right Cam .fits files: \n")

print()

image_num_list_left = []

time_stamp_list_left = []

image_num_list_right = []

time_stamp_list_right = []

image_num_left = 1 
##Left Camera
for file in glob.glob(Left_file_path + "\\" + Left_file_format + "*.fits"):
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
        image_num_list_left.append(image_num_left)
        time_stamp_list_left.append(file_time)
        
    image_num_left += 1 


image_num_right = 1 
##Right Camera
for file in glob.glob(Right_file_path+ "\\" + Right_file_format + "*.fits"):
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
        image_num_list_right.append(image_num_right)
        time_stamp_list_right.append(file_time)
        
    image_num_right += 1 


print("Flash appears in following Left Camera image numbers: \n")
for i in range(len(image_num_list_left)):
    print("Image Number: {}    Time Stamp: {}".format(image_num_list_left[i], time_stamp_list_left[i]))

print()

print("Flash appears in following Right Camera image numbers: \n")
for i in range(len(image_num_list_right)):
    print("Image Number: {}    Time Stamp: {}".format(image_num_list_right[i], time_stamp_list_right[i]))
