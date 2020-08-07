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

# initialize a total vote counter
total_votes = 0

# initialize list for candidate names
candidate_options = []

#initialize dictionary to hold votes for each candidate.  The name will be the key, votes the value
candidate_votes = {}

#winning candidate and winning count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#open the elction results and read the file.
with open(file_to_load) as election_data:
    #read the file oject with the reader function that comes with csv module
    file_reader = csv.reader(election_data)

    #skips the header row in the data file
    headers = next(file_reader)
    
    #interate through each row after the header in the csv file
    for row in file_reader:
        # add to the total vote count
        total_votes += 1
        #find candidate name from each row
        candidate_name = row[2]
        #if name does not match candidate added to the list already...
        if candidate_name not in candidate_options:
            #then add it to the list
            candidate_options.append(candidate_name)
            #begin tracking that candidates vote count 
            candidate_votes[candidate_name] = 0
        #add a vote to that candidate's count
        candidate_votes[candidate_name] += 1
    
    #iterate through candidate list
    #determine percentages for each person by looping through the counts
    for candidate_name in candidate_votes:
        # retrieve vote count of candidate
        votes = candidate_votes[candidate_name]
        #calculate vote percentage
        vote_percentage = float(votes) / float(total_votes) * 100
        #print name and vote percent
        print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,}) \n")

        #determine winning vote count and candidate
        #determing if the votes is greater than the winning count
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            #if true then..
            winning_count = votes
            winning_percentage = vote_percentage
            #and set winners name
            winning_candidate = candidate_name
    
    winning_candidate_summary = (
        f"------------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage: .1f}%\n"
        f"------------------------------\n")
    print(winning_candidate_summary)


#using the with statement open the file as a text file
#with open(file_to_save, "w") as txt_file:
    #write data to the file
    #txt_file.write("Counties in the Election\n-------------------------\nArapahoe\nDenver\nJefferson")
