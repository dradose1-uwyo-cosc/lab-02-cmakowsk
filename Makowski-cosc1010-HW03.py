# Name: Colter Makowski
# Lab Section: 15
# Submission Date 11/5/24
# Sources, help given to/received from
Calender = {"January": 31, "Febuary": 28, "March": 31, "April": 30, "May": 31,
 "June": 30, "July": 31, "August": 31, "September": 30, "October": 31, 
 "November": 30, "December": 31}

string = input("Enter date here in format **/**/****:")
while True:
    date = string.rsplit("/")
    print(date[2])
    y =int(date[2])-1
    #Jan first falls on day x where:
    day_1 = (36 + y +(y/4) - (y/100) + (y/400))%7
    print(int(day))
    
    #check if date is valid
    for key, value in Calender:
        if date[1] <= (Calender(date[0]), value:




    break