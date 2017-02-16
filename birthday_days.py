#Given your birthday and current day, calculate your age in days.
#Compensate for leap days, assume the birthday and current date are correct

days_of_months = [31,28,31,30,31,30,31,31,30,31,30,31]


print "IS THIS A LEAP YEAR?"
def isLeapYear(year):
   if year % 4 != 0 or (year % 100 == 0 and year % 400!=0) :
      return False
   else:
      return True

print isLeapYear(2000) # YES
print isLeapYear(2100) # NOT LEAP YEAR
print isLeapYear(2004) # YES
print isLeapYear(2013) # NOT LEAP YEAR



'''def days_month(month):    
    return days_in_month[month - 1]
  
print days_month(1)
print days_month(2)'''


print "THIS IS NOT USED"
def days_year(year):
    if isLeapYear(year) == True:
       return 366
    else:
       return 365
      
print days_year(2000)
print days_year(2004)
print days_year(2100)




'''
def daysBetweenDates(y1, m1, d1, y2, m2, d2):
     days_total = (d2 + days_month(m2)*m2 + days_year(y2)*y2)-
                  (d1 + days_month(m1)*m1 + days_year(y1)*y1)
 
     return days_total
'''

'''def sum_list(p):
       result = 0
       for e in p:
           result = result + e
           print result
print sum_list([44, 14, 76])'''


print"ADD DAYS FOR ALL MONTHS"
def month_total(a):
    total = 0
    for e in a:
       total = total + e
    return total

print month_total(days_of_months[:2]) #add all up to the 2nd months
print month_total([44, 14, 76])
print month_total(days_of_months[:12]) #add all up to the 12th months
 








print"ADD DAYS FOR ALL YEARS"

def year_total(y1,y2):
    years = range(y1,y2)
    total = 0
    for i in years:  #Prints out list of all years
       if isLeapYear(i) == True:
         total = total + 366
       else:
         total = total + 365
    return total

print year_total(1988,1989)#366 days,since 1988 is a leap year
print year_total(1989,1990)#365 days
print year_total(2000,2004)#366+365+365+365=1461, does not include2004




print range(1989,1999)  #prints out all the years


print"HOW MANY DAYS ALIVE AFTER ALL THIS TIME"

def daysBetweenDates(y1, m1, d1, y2, m2, d2):
    print "Days Alive!"
    MONTHS_BORN = month_total(days_of_months[:m1]) + d1
    print MONTHS_BORN
    
    MONTHS_CURRENT = month_total(days_of_months[:m2]) + d2
    print MONTHS_CURRENT
    
    return year_total(y1,y2) + MONTHS_CURRENT - MONTHS_BORN
#    return year_total(y1,y2) + (month_total(days_of_months[:m2] + d2)) - (month_total(days_of_months[:m1] + d1))
                
                                         

#print daysBetweenDates(1988, 0, 0, 1989, 0, 0)
#print daysBetweenDates(2003, 0, 0, 2005, 0, 0)
print daysBetweenDates(2005, 1, 10, 2005, 3, 20)
print daysBetweenDates(2000, 1, 1, 2004, 1, 1)
print daysBetweenDates(1988, 3, 22, 2016, 10, 20)
print daysBetweenDates(2000, 12, 31, 2001, 1, 2)


