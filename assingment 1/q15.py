#Write a program that reads data from a CSV file and prints it to the console.

import csv 
with open('data.csv',mode = 'r') as file:
        csvfile = csv.reader(file)
        for lines in csvfile:
                print(lines)
   
