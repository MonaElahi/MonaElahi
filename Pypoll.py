#Pypoll.py
# 1. The data we need to retrieve
# 2.The total number of votes cast
# 3. A complete list of  candidates who received votes
# 4. The percetage of votes each candidate won
# 5.The total number of votes each candidate won
# 6. The winner of the election based on popular vote
# 
##file_to_load = "election_results.csv" 
#election_data = open(file_to_load, 'r')

#election_data.close()

#with open(file_to_load) as election_data:

    #print(election_data)

'''import csv
import os

file_to_load = os.path.join("Election_Analysis","election_results.csv")

with open(file_to_load) as election_data:
    print(election_data)'''


import os
#path = "c:\Users\amakh\OneDrive\Desktop\Class folder\Election_Analysis\Pypoll.py"

file_to_save = os.path.join("analysis","election_analysis.txt")

with open(file_to_save) as "election_analysis.txt":
    outfile = open("file_to_save", "w")

outfile.write("Hello World")
outfile.write("hjhjhjhjh")

#open(file_to_save, "w")    
outfile.write("How are you")
outfile.write("test")
outfile.write("market")
outfile.write("market")