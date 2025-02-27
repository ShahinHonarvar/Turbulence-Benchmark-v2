def if_perfect_num(lst):
    """
    if_perfect_num takes one argument, a list of positive integers, and returns true if the integer at index 8 is a perfect number, otherwise, it should return false.
    """
    num = lst[8]
    sum_of_divisors = 0
    for i in range(1, num):
        if num % i == 0:
            sum_of_divisors += i
    return sum_of_divisors == num