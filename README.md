# Find_Flashes
2 Python programs to find .fits files where flashes are present as well as their respective Timestamp. First file is intended for finding flash from one camera, the second finds flashes from 2 separate cameras. 

## Program Method

### Step 1: 

The program looks through every column of every .fits file being looked at and takes the average of each column. These averages are then appended to a list to be further analyzed. 

### Step 2: 

The program looks through the list of the average column value for every column of the .fits file. If the ratio between the average value of all the column and the value of an individual column is less than 0.1, it considers that column to be a "flash". If 5 or more columns in the .fits value are registered to be a flash, the program considers the .fits file in question to be an image where a flash is present and the file number and timstamp are logged. 

### Step 3: 

After checking each .fits file, any files which have been registered to have flashes present are printed out along with their respective timestamp. 

## How to Run: 

These files can be run through either an IDE like Spyder, Visual Studio, VScode etc or run directly through a command prompt. You will be prompted first to enter the path to the directly where the .fits files you want to process are located. For example, if your .fits file are located in "C:\Documents\Camera_Data", you would input C:\Documents\Camera_Data. The program will then ask you to enter the format of the .fits files you want to look at. For example, if your .fits files are named "Left_cam1.fits, Left_cam2.fits, Left_cam3.fits etc...", you can enter anything that would capture the general format, such as "Left_". The program will then look for files in the directory you inputted earlier which begin with "Left_" and are .fits files. 

This is the same process for both the onecam and twocam files. The only difference is the twocam file runs this process twice for multiple cameras, so you will have to fill out this information multiple times to have the program look at data from 2 cameras as opposed to one. 
