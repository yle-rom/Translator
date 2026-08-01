#def main 
#int salary
#int hoursOfWork
#int daysOfWork
hoursOfWork = int(input())
daysOfWork	= int(input())
salary = hoursOfWork*daysOfWork*5 + 100
if salary < 750 :
	salary  = 750 
print(salary)