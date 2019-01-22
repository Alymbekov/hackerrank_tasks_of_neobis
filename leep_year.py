# We add a Leap Day on February 29,
#  almost every four years.
#   The leap day is an extra, or intercalary 
#   day and we add it to the shortest month of the
#    year, February.
# In the Gregorian 
# calendar three criteria must be
#  taken into account to identify leap years:
# The year can be evenly divided by 4,
#  is a leap year, unless:
# The year can be evenly divided by 100,
#  it is NOT a leap year, unless:
# The year is also evenly divisible by 400.
#  Then it is a leap year.
# This means that in the Gregorian calendar, 
# the years 2000 and 2400 are leap years, 
# while 1800, 1900, 2100, 2200, 2300 and 2500 are NOT leap years.Source
# Task
# You are given the year, and you have to write 
# a function to check if the year is leap or not.
# Note that you have to complete the function 
# and remaining code is given as template. 

# def is_leap(year):
#     leap = False
#     notleap = True
#     check_a_leap_year = year % 4 == 0
#     second_check = year % 400 == 0
#     third_check=year % 100== 0
#     if year == check_a_leap_year:
#         return(notleap)
#     elif year == second_check:
#         return(notleap)
#     elif year == third_check:
#         return(leap)
#     else:
#         return leap
#def is_leap(year):    
    #if year%4==0 and year%400==0 and year%100!=0:
       # return True
   # else:
        #return False
def is_leap(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    else:
        return False
year = int(input())
print(is_leap(year))