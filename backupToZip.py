#! python3
# backupToZip.py - Copies an entire folder & its contents into
# a ZIP file whose filename increments.

import zipfile, os 

def backupToZip(folder):
    # Back up the entire contents of "folder" into a ZIP file.

    folder = os.path.abspath(folder) # make sure folder is absolute

    # Figure out the filename this code should use based on
    # what files already exist.
    number = 1
    while True:
        zipFilename = os.path.basename(folder) + '_' + str(number) + '.zip'
        if not os.path.exists(zipFilename):
            break # the first nonexistent filename found will cause the loop to break
        number += 1

    # TODO: Create the ZIP file.
    print(f'Creating {zipFilename}...')
    backupZip = zipfile.ZipFile(zipFilename, 'w')

    # TODO: Walk the entire folder tree and compress the files in each folder.
    for foldername, subfolders, filenames in os.walk(folder): #use os.walk() in a for loop and on each iteration it will return the iteration's current folder name, the subfolders in that folder and the filenames in taht folder
        print(f'Adding files in {foldername}...')
        # Add the current folder to the ZIP file.
        backupZip.write(foldername) #the folder is added to the ZIP file

        #Add all the files in this folder to the ZIP file.
        for filename in filenames: # the nested for loop can go through each filename i nthe filenames list
            newBase = os.path.basename(folder) + '_'
            if filename.startswith(newBase) and filename.endswith('.zip'):
                continue # don't back up the backup ZIP files
            backupZip.write(os.path.join(foldername, filename))
    backupZip.close()
    print('Done.')

backupToZip('C:\\Users\\mmcclain\\delicious')