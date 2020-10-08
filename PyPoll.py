import csv
import os
# #assign a variable for the file to load and the path
file_to_load = os.path.join('election_results.csv')
# #open the election results and read the file
with open(file_to_load) as election_data:
    
    #to do: read and analyze the data here
    #read the file object with the reader function
    file_reader = csv.reader(election_data)
    #read and print he header row
    headers = next(file_reader)
    print(headers)

#create a filename variable to a direct or indirect path to the file
file_to_save = os.path.join('analysis','election_anaylsis.txt')
#using the with statement tp open the file as a text file
with open(file_to_save, 'w') as txt_file:
    #write three counties to the file
    txt_file.write('Counties in the Election\n------------------------\nArapahoe\nDenver\nJefferson ')

    

