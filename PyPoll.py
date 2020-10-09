import csv
import os
#assign a variable for the file to load and the path
file_to_load = os.path.join('election_results.csv')
#Assign a variable to save the file as a path
file_to_save = os.path.join('analysis','election_anaylsis.txt')
#1. Initialize a total vote counter
total_votes = 0

#candidate options
candidate_options = []
# 1. Declare the empty library
candidate_votes = {}

#winning candidate and winning count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#open the election results and read the file
with open(file_to_load) as election_data:
    #read the file object with the reader function
    file_reader = csv.reader(election_data)
    #read the he header row
    headers = next(file_reader)
    # print each row in the CSV file.
    for row in file_reader:
        #2. Add to the total vote count
        total_votes += 1
        # print the candidate name from each row.
        candidate_name = row[2]
        # if the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
            #add to the candidate list
            candidate_options.append(candidate_name)
            #begin tracking that candidate's vote count
            candidate_votes[candidate_name] = 0
        # add a vote to that candidate's count
        candidate_votes[candidate_name] += 1
        #save the results to our text file.
with open(file_to_save, "w") as txt_file:
    #print the final vote count to the terminal
    election_results = (
        f"\nElection Results\n"
        f"------------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"------------------------------\n")
    print(election_results, end="")
        
            
    #save final vote count to the text file
    txt_file.write(election_results)
    #determine the percentage of votes for each candidate by looping through the counts
    #1. iterate through the candidate list.
    for candidate_name in candidate_votes:
        #2 Retrieve vote count of a candidate
        votes = candidate_votes[candidate_name]
        #3 calculate the percentage of votes
        vote_percentage = float(votes) / float(total_votes) * 100
        #4 print the candidate name and the percentage of votes
        #print(f"{candidate_name}: received {vote_percentage}% of the vote")
        candidate_results= (
            f"{candidate_name}: {vote_percentage:.1f}%({votes})\n")
        # print out each name, vote count, and percentage of votes to terminal
        #print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        print(candidate_results)
        txt_file.write(candidate_results)
    
        #determine if the votes is greater than the winning count
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            #if true then set winning_count = votes and winning_percent= vote_percentage
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name       

    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning_Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    txt_file.write(winning_candidate_summary)