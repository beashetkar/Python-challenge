# You oversee hundreds of employees across the country developing Tuna 2.0, 
# a world-changing snack food based on canned tuna fish.
#  Alas, being the boss isn't all fun, games, and self-adulation. 
# The company recently decided to purchase a new HR system, and unfortunately for you, 
# the new system requires employee records be stored completely differently.

# Your task is to help bridge the gap by creating a Python script able to convert your employee
#  records to the required format. Your script will need to do the following:

# 1) Import the employee_data1.csv and employee_data2.csv files,
# 2) Convert and export the data.


import os
import csv
import datetime

# Function to look in state dictionary for the abbreviation and return it.

def state_abbrev(state_name):
    
    us_state_abbrev = { 'Alabama': 'AL', 'Alaska': 'AK', 'Arizona': 'AZ',
                        'Arkansas': 'AR','California': 'CA','Colorado': 'CO',
                        'Connecticut': 'CT', 'Delaware': 'DE', 'Florida': 'FL',
                        'Georgia': 'GA', 'Hawaii': 'HI', 'Idaho': 'ID',
                        'Illinois': 'IL', 'Indiana': 'IN', 'Iowa': 'IA',
                        'Kansas': 'KS', 'Kentucky': 'KY', 'Louisiana': 'LA',
                        'Maine': 'ME', 'Maryland': 'MD',  'Massachusetts': 'MA',
                        'Michigan': 'MI', 'Minnesota': 'MN', 'Mississippi': 'MS',
                        'Missouri': 'MO', 'Montana': 'MT', 'Nebraska': 'NE',
                        'Nevada': 'NV', 'New Hampshire': 'NH', 'New Jersey': 'NJ',
                        'New Mexico': 'NM', 'New York': 'NY', 'North Carolina': 'NC',
                        'North Dakota': 'ND', 'Ohio': 'OH', 'Oklahoma': 'OK',
                        'Oregon': 'OR', 'Pennsylvania': 'PA', 'Rhode Island': 'RI',
                        'South Carolina': 'SC', 'South Dakota': 'SD', 'Tennessee': 'TN',
                        'Texas': 'TX', 'Utah': 'UT', 'Vermont': 'VT', 'Virginia': 'VA',
                        'Washington': 'WA', 'West Virginia': 'WV',  'Wisconsin': 'WI',
                        'Wyoming': 'WY' }

    return (us_state_abbrev.get(state_name))
  
# Give  the employee.csv file to convert.

input_file = input("Enter the input employee.cvs  file  to analyze: ")

# Look for the input csv file in Resources directory

input_path = os.path.join("Resources", input_file)

# Output File

output_file = input("Enter the output_employee.cvs  file: ")

output_path = os.path.join("Output", output_file)

try:
    # Open both files input.csv and output.csv file
    # 	
    with open(input_path,'r', newline='') as input_csv, open(output_path,'w') as output_csv:
	
        # Initialize output csv.writer 
        csvwriter = csv.writer(output_csv, delimiter =',')
    
        # CSV reader specifies delimiter and variable thet holds contents
        csvreader = csv.reader(input_csv,delimiter=',')

	    # Skip the first row of the csvreader
        next(csvreader, None)
    
        # Write the first row (column headers) in csvwriter
        csvwriter.writerow(('Emp ID', 'First Name', 'Last Name', 'DOB', 'SSN', 'State'))
   
        # Read each Row of csvreader and do the required conversions

        for r in csvreader:

            # Copy the Emp ID to a variable
            emp_id = r[0]

            # Convert column Name to 'First Name' and  'Last Name'
            # and check if name it is not empty
         
            fullname_lst = []
            fullname_lst = r[1].split(' ')
            name = fullname_lst[0]
            lastname = fullname_lst[1]
                     
            # Convert column DOB fomat mm/dd/yyyy to dd/mm/yyyy

            from datetime import datetime
            dob = datetime.strptime(r[2] , '%Y-%m-%d')
            dob = datetime.strftime(dob, "%m/%d/%Y")
                    
            # Format SSN ***-**-****    
            ssn_lst =[]
            ssn_lst = r[3].split('-')
            ssn = ("***-**-"+ ssn_lst[2])
         
            # Call function  state_abbrev for modifiyin format of state

            st_abv=state_abbrev(r[4])
     
            # Print to output file
            print ( emp_id + " " + name + " " + lastname  + " " + dob  + " " + ssn  + " " + st_abv)
            csvwriter.writerow((emp_id, name, lastname, dob, ssn, st_abv))

except:
    print ("File : " + input_file + " cannot find in : " + input_path)
    exit()        
        
               
            

            







