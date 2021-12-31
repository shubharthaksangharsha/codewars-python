#https://www.codewars.com/kata/514b92a657cdc65150000006/train/python
def solution(number):
    sum = 0 #taking a sum variable to get the sum of all variables
    for i in range(2,number):
        if i % 3 == 0 or i % 5 == 0: #checking the condition using % 
            sum+=i  #adding i to sum variable if it's a divisble by 3 or 5           
        else:
            pass #if not then pass it 
    return sum #returning the sum variable 

    
