def leapyear(year):
    
    return (year%400 == 0) or (year%4==0 and year%100!=0)
print(leapyear(2090))
       