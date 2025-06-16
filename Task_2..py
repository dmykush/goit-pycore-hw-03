import random

def get_nambers_ticket(min_num, max_num, quantity):
    if min_num < 1 or max_num > 1000 or min_num > max_num:
        return[]
    if quantity < 1 or quantity > (max_num - min_num + 1):
        return[]
    
    numbers = random.sample(range(min_num, max_num + 1), quantity)
    numbers.sort()
    return print(numbers)

get_nambers_ticket(1, 49, 6)

