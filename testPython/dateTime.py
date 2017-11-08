import datetime

today = datetime.date.today()
print(today)
print(today.year)
print(today.day)
print(today.month)

# specifying datetime format with strftime

print(today.strftime("%d %b %m %Y"))

#long line break with \

print("this is line one "
      +"this is line  2")

# birthday
userInput = input("please input your birthday (d/m/yyyy):")
birthday = datetime.datetime.strptime(userInput, "%d %m %Y").date()
print(birthday)

currentDate = datetime.date.today()

days = birthday - currentDate

print(days.days)