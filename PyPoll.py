# Data we need to retrieve.
# 1. Total number of votes cast
# 2. Complete list of candidates who recieved votes.
# 3. Percentage of votes for each candidate.
# 4. Total number of votes for each candidate.
# 5. Winner of the election by popular vote.

import csv
import os
#assigns a variable for the file to load and the path(when the path is unknown)
file_to_load = os.path.join("resources", "election_results.csv")

#assigns a filename variable to an indirect path to the file
file_to_save = os.path.join("analysis", "election_analysis.txt")

#open the elctions results and read the file.
with open(file_to_load) as election_data:
    #read the file oject with the reader function that comes with csv module
    file_reader = csv.reader(election_data)
    #read and print the header row
    headers = next(file_reader)
    print(headers)


#using the with statement open the file as a text file
#with open(file_to_save, "w") as txt_file:
    #write data to the file
    #txt_file.write("Counties in the Election\n-------------------------\nArapahoe\nDenver\nJefferson")
