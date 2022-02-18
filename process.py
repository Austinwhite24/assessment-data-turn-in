log_file = open("um-server-01.txt") #this is opening up and calling the other um-server file, this is where we are pulling are data from.


def sales_reports(log_file): #this is giving a function a name of sales_reports and its passing in all the data from log_file which we got from the server file

    for line in log_file: # this is getting each line or row in log_file and caliing it line
        line = line.rstrip() #this is going through every line and is returning a copy of the data, we could also pass in any characters inside if we wanted them to be stripped away from the data we grab

        day = line[0:3] #giving a variable day to = the line at index 0 which is the begining of the line and it goes over 3 indexes 
        if day == "Mon": # if index [0:3] starts with Mon
            print(line) #if thats true up there than print it out 


sales_reports(log_file) #run the function sales_report and pass in all of (log_file)'s data.
