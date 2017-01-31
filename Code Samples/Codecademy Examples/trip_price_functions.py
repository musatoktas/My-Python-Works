Python 3.6.0b3 (default, Nov  1 2016, 03:21:01) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def hotel_cost(nights):
    return 140 * nights

def plane_ride_cost(city):
    if city == "Charlotte":
        return 183
    
    elif city == "Tampa":
        return 220
    
    elif city == "Pittsburgh":
        return 222
    
    elif city == "Los Angeles":
        return 475
        
def rental_car_cost(day):
    rent = 40 * day
    if day >= 7:
        return 40 * day - 50
    elif day >= 3: 
        return 40 * day -20
    else:
        return 40 * day
    

def trip_cost(city, days, spending_money):
        print plane_ride_cost(city) + hotel_cost(days) +  rental_car_cost(days) + spending_money
