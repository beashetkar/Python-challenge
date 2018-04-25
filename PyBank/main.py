# You will be given two sets of revenue data:
# (budget_data_1.csv and budget_data_2.csv). 
# Each dataset is composed of two columns: Date and Revenue. 

# Your task is to create a Python script that analyzes the records to calculate each of the following:
# •	The total number of months included in the dataset
# •	The total amount of revenue gained over the entire period
# •	The average change in revenue between months over the entire period
# •	The greatest increase in revenue (date and amount) over the entire period
# •	The greatest decrease in revenue (date and amount) over the entire period

import os
import csv

# Function that helps to format the amount pass

def as_currency(amount):
    if amount >= 0:
        return '${:.2f}'.format(amount)
    else:
        return '-${:.2f}'.format(-amount)

# Give the csv file to analyze 

input_csv = input("Enter the input file.csv name to analyze: ")

# Give the output text file.txt 

output_txt = input("Enter the output file.txt name: ") 

# Look for the input csv file in Resources directory

input_path = os.path.join("Resources", input_csv)

try:

	# Open the CSV	
	with open(input_path,'r', newline='') as csvfile:
	
		# CSV reader specifies delimiter and variable thet holds contents
		csvreader = csv.reader(csvfile,delimiter=',')
	
		# Skip the first row of the csv
		next(csvreader, None)
	
		total_months = 0
		total_revenue = 0
		past_revenue = 0
		revchangedict= {}
		change_revenue = 0
				
		# Reading each row of each file and calculate the total months and the 
    	# total revenue, insert the month and the change of revenue in the 
    	# dictionary revchangedict 

		for row in csvreader:
			
			total_months += 1
			total_revenue += int(row[1])
		
			if past_revenue != 0:
				change_revenue = int(row[1]) - past_revenue
				revchangedict.update({row[0]:change_revenue})
			else :
				revchangedict.update({row[0]:0})

			past_revenue = int(row[1])
    
except:
    print ("File : " + input_csv  + " cannot find in : " + csvpath)
    exit()

greatest_decr_revenue = 0
greatest_incr_revenue = 0
av_revenue_change = 0

# loop through revchangedict dictionary 
# 				
for key, value in revchangedict.items():
	
	# Find the greatest increase in revenue ( date and amount)

	if  value >= greatest_incr_revenue: 
		greatest_incr_revenue = value
		month_incr = key

	# Find the greatest decrease in revenue ( date and amount).
	elif value <= greatest_decr_revenue:
		greatest_decr_revenue = value
		month_decr = key

	# Calculate the average change

	av_revenue_change+= float(value)
	past_revenue = value
	
av_revenue_change = float(av_revenue_change / total_months)
	
# print the final results to terminal

print ("Financial Analysis")
print ("------------------------------------------------")
print ("Total Months: " + str(total_months))
print ("Total Revenue: " + str(as_currency(total_revenue)))
print ("Average Revenue Change: " +  str(as_currency(av_revenue_change)))
print ("Greatest Increase in Revenue: " + str(month_incr) + "  (" + str(as_currency(greatest_incr_revenue)) +")")
print ("Greatest Decrease in Revenue: " + str(month_decr) + "  (" + str(as_currency(greatest_decr_revenue)) + ")")	


output_path = os.path.join("Output", output_txt)

# Open the file using "write" mode. Specify the variable to hold the contents

with open(output_path, "w", newline='') as txtfile:

   # Write the first row "Header of the File
	txtfile.write("Financial Analysis \n")
	txtfile.write("------------------------------------------------\n")

	# Write the results in the next rows
	txtfile.write("Total Months: " + str(total_months) + "\n")
	txtfile.write("Total Revenue: " + str(as_currency(total_revenue)) + "\n")
	txtfile.write("Average Revenue Change: " +  str(as_currency(av_revenue_change))+ "\n")
	txtfile.write("Greatest Increase in Revenue: " + str(month_incr) + "  (" + str(as_currency(greatest_incr_revenue)) +") \n")
	txtfile.write("Greatest Decrease in Revenue: " + str(month_decr) + "  (" + str(as_currency(greatest_decr_revenue)) + ") \n")
    
