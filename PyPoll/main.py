# You are tasked with helping a small, rural town modernize its vote-counting process. 
#  (Up until now, Uncle Cleetus had been trustfully tallying them one-by-one,
#  but unfortunately, his concentration isn't what it used to be.)
#
# You will be given two sets of poll data (election_data_1.csv and election_data_2.csv). 
# Each dataset is composed of three columns: Voter ID, County, and Candidate. 
# Your task is to create a Python script that analyzes the votes and calculates each of the following:

# 1) The total number of votes cast
# 2) A complete list of candidates who received votes
# 3) The percentage of votes each candidate won
# 4) The total number of votes each candidate won
# 5) The winner of the election based on popular vote.

import os
import csv

# Give the csv file or poll data to analyze in PyPoll directory

input_file = input("Enter the input poll data (file.csv) to analyze: ")

# Give the output text file.txt 

output_file = input("Enter the output file.txt name: ") 
		
csvpath = os.path.join("Resources", input_file)

try:
 
	with open(csvpath,newline='') as csvfile:
	
		# CSV reader specifies delimiter and variable thet holds contents
		csvreader = csv.reader(csvfile,delimiter=',')
	
		# Skip the first row of the csv
		next(csvreader, None)
	
		total_num_votes = 0
		candidate_dict = {}
				
		# Reading each row of input file  
    	
		for row in csvreader:
			
			# Calculate the total mnumber of votes to cast
			total_num_votes += 1
 
			# Check if candidate already exists in dictionary and add a vote
			if row[2] in candidate_dict.keys():
				candidate_dict[row[2]] +=1
		
			# Insert the candidate as a key in dictionary 
			# and initialize how many votes he/she has	
			else:       
				candidate_dict.update({row[2]:1})

except:
    print ("File cannot be opened: " + filename)
    exit()


# loop through candidate_dict dictionary to get the following information:
# 1) A complete list of candidates who received votes
# 2) The total number of votes each candidate won
# 3) The percentage of votes each candidate won
# 4) The winner of the election based on popular vote.

percentage_votes = 0
winner_votes = 0

# Specify the file to write the final results

txtpath = os.path.join("Output", output_file)

# Open the file using "write" mode. Specify the variable to hold the contents
with open(txtpath, 'w', newline='') as txtfile:

	# print the final results
	print ("Election Results")
	print ("------------------------------------------------")
	print ("Total Votes: " + str(total_num_votes))
	print ("------------------------------------------------")

	# Write down results to text file
	txtfile.write("Election Results \n")
	txtfile.write("------------------------------------------------\n")
	txtfile.write("Total Votes: " + str(total_num_votes) + "\n")
	txtfile.write("------------------------------------------------\n")

	# Loop through the candidate dictionary to get winner, votes per candidate and percentage
				
	for key, value in candidate_dict.items():
	
		# find the winner

		if value > winner_votes:
			winner_votes = value
			winner = key
	
		# Calculate the percentage of votes each candidate won

		percentage_votes = float(value/total_num_votes)*100

		print ( key + " : "  + str("{0:.0f}%".format(percentage_votes)) + " ( " + str(value) + " )" )
		txtfile.write( key + " : "  + str("{0:.0f}%".format(percentage_votes)) + " ( " + str(value) + " ) \n" )

	# print the final results

	print ("------------------------------------------------")
	print ( " Winner: " +   winner)
	print ("------------------------------------------------")

	txtfile.write("------------------------------------------------\n")
	txtfile.write( " Winner: " +  winner  + "\n")
	txtfile.write("------------------------------------------------\n")