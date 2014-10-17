#### TxtToCsvMerger ####
# Simple, inefficient and broken script to merge text files
# into somewhat broken CSV's of two columns. Currently does
# not output good csv's that can be easily recognized by
# MS Excel. Written to specifically target specific documents.

# This code does not include any guarantee to work.

# By Lichi Li

import glob
files = glob.glob( '*/*.txt' ) #Look for all txt's in all subfolders

import csv

def csv_writer(data, path):
    """
    Write data to a CSV file path
    """
    with open(path, "wb") as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        for line in data:
            writer.writerow(line)

if __name__ == "__main__":

    path = "output.csv"
    
    data = [] # Container of the entire data set.
    
    for file_ in files:
        newDataRowforOneFile = []
        newDataRowforOneFile.append(file_)
        documentBody = ""
        for line in open( file_, 'r' ):
            line = line.replace("\n", "")
            documentBody = documentBody + line

        newDataRowforOneFile.append(documentBody)
        data.append(newDataRowforOneFile)
    
    csv_writer(data, path)
        
