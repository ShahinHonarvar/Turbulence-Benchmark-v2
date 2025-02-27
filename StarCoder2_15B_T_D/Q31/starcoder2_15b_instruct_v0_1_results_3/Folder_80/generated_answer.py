def if_perfect_num(lst):
    """
    Returns True if the integer at index 746 is a perfect number, otherwise returns False.
    """
    num = lst[746]
    sum_of_divisors = 0
    for i in range(1, num):
        if num % i == 0:
            sum_of_divisors += i
    return sum_of_divisors == num