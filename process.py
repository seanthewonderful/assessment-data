log_file = open("um-server-01.txt") 
# Open the file "um-server-01.txt" to be able to make use of it with our code in this file


def sales_reports(log_file): # Creating a function(def=defining) called sales_report taking in a parameter, "log_file"
    for line in log_file: # Indent to run as the function. Iterate through each line in log_file and do the following:
        line = line.rstrip()
        day = line[0:3]
        if day == "Tue":
            print(line)


sales_reports(log_file)

