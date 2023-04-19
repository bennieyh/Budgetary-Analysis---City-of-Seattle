

# Budgetary Analysis - City of Seattle
# Scenario
# The Office of the Inspector General for the City of Seattle has commissioned an investigatory audit of the City's budget and appropriations over the 2012 fiscal year. 
#The goal of this audit is to show the total funds spent by each department. Naturally, you have selected Python for this project. 

# Tasks
# Download the CSV file containing the budget and appropriations data for the 2012 fiscal year. 
# We went ahead and collected this file from Data.gov for you. Download the files here:
# 2012 Expenditures for the City of Seattle
# Review the CSV file to determine what each column of data represents. 
# Hint: Some important columns: Department, 2012 Actual
# Aggregate (sum) how much money was spent by each department. Hint: you can use a dictionary to store a list of expenses for each department.
# Print the results to the screen as neatly as possible. For example, you can simply print the department, a white-space character (tab or space), 
#then the sum of that department's expenses.
# Zip up your Python project and submit your assignment on this page.
# Click the Start Assignment button at the top of the screen. This will allow you to upload your project at the bottom of the page.
# Caveats
# You must use Python for this assignment. The only work you should do in Excel is cleaning up the data if needed.
# All dollar amounts must be properly formatted: $1,000,000.00
# Project Submission
# You must submit a .zip file containing all of your Python code or a GitHub URL for your code on GitHub.com 
# You may include additional artifacts to support your project as you see fit.



#################################           *           ################################# 
#################################        *      *          ################################# 
#################################           *           ################################# 
#################################        *  *   *          ################################# 



import csv

#class DepartmentExpenses:
    # Class variables
#    columns = ['Department', 'BCL', 'Program', '2012']
#   year_column = '2012'

#    def __init__(self, department, bcl, program, expenses):
        # Instance variables
#        self.department = department
#        self.bcl = bcl
#        self.program = program
#        self.expenses = expenses


######################################################################################################################################
####### THE CODE IN BELOW IS TO HELP ME SEE IF THE PROGRAM CAN READ THE FILE AND OUTPUT THE FILE DATA ######
######################################################################################################################################
#data_dict = {}  # create an empty dictionary

# process CSV file and add data to dictionary
#with open('ChallengePythonProject.csv', 'r') as file:
    #for line in file:
        # split the CSV line into fields
        #fields = line.strip().split(',')
        
        # assume the first field is the key
        #key = fields[0]
        
        # assume the remaining fields are values
        #values = fields[0:4]
        
        # add the values to the dictionary
        #data_dict[key] = values
        #print(data_dict[key])
######################################################################################################################################
####### THE CODE IN ABOVE IS TO HELP ME SEE IF THE PROGRAM CAN READ THE FILE AND OUTPUT THE FILE DATA ######
######################################################################################################################################


import csv

#define variables and methods related to ProgramExpenses.
class ProgramExpenses:
    # Class Variables
    # column is the list that defines data to be processed
    columns = ['Department', 'BCL', 'Program', '2012']
    # year_column is a string to use to retrieve the values of the year column from the CSV
    year_column = '2012'

# the '__init__' is a method in python that gets called autoamtically when an object is created. In this case it intializes the instance 'ProgramExpenses'
    def __init__(self, department, bcl, program, expenses):
        self.department = department
        self.bcl = bcl
        self.program = program
        #self.year = year
        self.expenses = expenses

       # Format a literal dollar sign at the beggining of the string expenses eg 10405 to $10405 
    def format_expenses(self):
        return '${:,.2f}'.format(self.expenses)
    
    #Here we read the data in the CSV and return an instance of the class with parsed data : parse == converting
    #Here the data in the row was converted into integer: then returns an instance of class using 'cls' parameter to the the constructor
    def from_csv_row(cls,row):
        expenses = int(row[cls.year_column])
        return cls(expenses)
    
# Here we create an empty list that will be used to store instances of ProgramExpenses
expenses_list = []

# Read the CSV file mean this command will open our file named below as we are using the open () function which returns a file object
# !!!!By using 'with here it ensures that the file is properly closed after it has been used!!!

with open('city-of-seattle-2012-expenditures-dollars.csv') as csv_file:

# Here the csv_reader() function is used to create a reader object, which iterate over the content of the CSV file row by row
#The delimeter is used to specify that the values are separated by a comma
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    
    # Iterate through each row of the CSV file
    for row in csv_reader:
        if line_count == 0:
            # Skip the header row
            line_count += 1
        else:
            # Create an instance of the ProgramExpenses class
            department = row[0]
            bcl = row[1]
            program = row[2]
            #year = int(row[3])
            # Here if the value in the column year is empty: the value will be set to 0.0
            expenses = 0.0
            if row[3] != '':
                expenses = float(row[3])
            program_expenses = ProgramExpenses(department, bcl, program, expenses)
            
            # Add the instance to the expenses list
            #This appends the instance of the ProgramExpenses class which represent the expenses of a particular department
            expenses_list.append(program_expenses)
            
            #This increment the line_count variable by 1 for each row of the CSV file: helps to keep track of the number of rows processed
            line_count += 1
    
    # Create a dictionary to store the aggregated expenses by department
    # Here this command creates an empty dictionary called 'department_expenses'
    department_expenses = {}

    # then it loops thorugh each object: remeber the 'for loop'
    for year in expenses_list:

        #This means if the expense value of the object exsists in the expenses value it appends that object in the department expenses dictionary.
        if year.department in department_expenses:
            department_expenses[year.department].append(year.expenses)
            #Else if the object does not exsist it creates one and assign it to the new department expense in the dictionary
        else:
            department_expenses[year.department] = [year.expenses]
            
    # Print the results
    print("Department\tTotal Expenses")
    print("---------\t--------------")
    for department, expenses in department_expenses.items():
        total_expenses = sum(expenses)
        formatted_expenses = '${:,.2f}'.format(total_expenses)
        print(f"{department}\t\t{formatted_expenses}")



