def if_perfect_num(lst):
    """
    This function takes a list of positive integers as input and returns True if the integer at index 222 is a perfect number, otherwise it returns False.
    """
    num = lst[222]
    sum_of_divisors = 0
    for i in range(1, num):
        if num % i == 0:
            sum_of_divisors += i
    if sum_of_divisors == num:
        return True
    else:
        return False