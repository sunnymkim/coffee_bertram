import sys,pprint


def roundPrices(prices : list):
    rounded_prices = []
    for price in prices:
        dec = price % 1 #remove decimal
        if dec <= 0.25: #round down to whole number
            rounded_prices.append(price-dec)
        elif dec > 0.25 and dec <=0.75: #round to nearest .5
            rounded_prices.append(price-dec + 0.50)
        else: #round up to whole number
            rounded_prices.append(price-dec+1)
    return rounded_prices

def createCalendar (people : list, prices : list, n : int): #n = number of people
    rounded_prices = roundPrices(prices) #round prices to nearest .5 (makes calculating ratios easier)
    days_per_person = [(2*price) for price in rounded_prices] #mult price by 2 to make number of days a whole number
    total_days = sum(days_per_person) #total number of days in one paying cycle

    #We want to calculate the amount of money each person pays extra or does not pay for transparency"""
    ratios = [(day/total_days) for day in days_per_person] #ratio of number of day person pays to the total number of days
    actual_ratios = [(price/sum(prices)) for price in prices] #actual ratio of price of coffee to total price
    diff_per_person = [(ratio-actual_ratio) for (ratio,actual_ratio) in zip(ratios,actual_ratios)] #calculate difference per person

    schedule = []
    days_left = days_per_person.copy() #make a copy of days_per_person to keep original list
    p = 0 #index of person
    for i in range(0, int(total_days)): #loop through entire cycle
        
        """
        We loop through to find next person who still has days left to pay for. 
        We know this loop will terminate because total_days is the sum of all entires of days_left,
        so by the time all people have paid, the outer for loop will terminate.
        """
        while(days_left[p%n] <= 0): #mod p by n so it does not go out of bounds
            p += 1
        schedule.append(people[p%n]) #add person to schedule
        days_left[p%n] -= 1 #decrease number of days left to pay for person p%n by 1
        p += 1 #increase p so next person in the list pays (spread out days that each person pays)
    return schedule, days_per_person, diff_per_person

"""
Read input from input file
"""
f = open("input.txt", "r")
n = int(f.readline())
people = f.readline().split()
prices_string = f.readline().split()
prices = [float(price) for price in prices_string]

#RUN MAIN FUNCTION
schedule, days_per_person, diff_per_person = createCalendar(people, prices,n) 

"""
Input from Terminal
"""
day = input("TODAY'S DAY COUNT: ")
while not day.isnumeric(): 
    print("invalid day! (not a whole number)")
    day = input("TODAY'S DAY COUNT: ")
print(schedule[(int(day)-1)%len(schedule)] + " pays today!")
input_str = input("EXTRA INFO? (Y/N) ")
if(input_str == 'Y'):
    print("There are " + str(n) + " in the current employee list.")
    for i in range(0,n):
        print("Person " + str(i+1) + ":")
        print("Name: " + people[i])
        print("Price of drink: " + str(prices[i]))
        print("Amount overpaid/underpaid per day: " + str(diff_per_person[i]))
else:
    print("HAVE A NICE DAY!")



