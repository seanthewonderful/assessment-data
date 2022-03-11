log_file = open("um-server-01.txt") 
# Open the file "um-server-01.txt" to be able to make use of it with our code in this file


def sales_reports(log_file): # Creating a function(def=defining) called sales_report taking in a parameter, "log_file"
    for line in log_file: # Indent to run as the function. Iterate through each line in log_file and do the following:
        line = line.rstrip() # Removing the white space at the end (right side) of each line string
        day = line[0:3] # Setting variable day = the first 3 characters of each line. Starts at string position 0, prints 3 characters.
        # if day == "Tue": # Creating condition if those first 3 characters match "Tue", then do the following
        if day == "Mon": # New code per directions to print sales info for Mon instead
            print(line) # Print the entire line to the console.


sales_reports(log_file) # Invoking the function with the file "log_file" as its parameter, through which this function will be able to iterate

