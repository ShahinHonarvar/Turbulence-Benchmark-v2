def if_perfect_num(lst):
    """
    Returns True if the integer at index 312 is a perfect number, otherwise returns False.
    """
    num = lst[312]
    sum_of_divisors = 0
    for i in range(1, num):
        if num % i == 0:
            sum_of_divisors += i
    return sum_of_divisors == num