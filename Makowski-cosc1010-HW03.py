# Name: Colter Makowski
# Lab Section: 15
# Submission Date 11/5/24
# Sources, help given to/received from

string = input("Enter date here in format **/**/****:")
while True:
    date = string.rsplit("/")
    month = int(date[0])
    day = int(date[1])
    year = int(date[2])
    def is_leap_year(year):
        return (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0))
    #check if date is valid
    y = int(year) - 1
    jan_first = (36 + y + (y // 4) - (y // 100) + (y // 400)) % 7
    days_in_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap_year(year):
        days_in_months[1] = 29
    if month < 1 or month > 12:
        print(f"{string} Invalid Date")
        break
    if day < 1 or day > days_in_months[month - 1]:
        print(f"{string} Invalid Date")
        break
    else: 
        days_of_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
        total_days = sum(days_in_months[:month - 1]) + (day - 1)
        day_of_week = (jan_first + total_days) % 7
        day_of_weak = days_of_week[day_of_week]
        print(f"{date[0]}/{date[1]}/{date[2]} {day_of_weak}")
    break