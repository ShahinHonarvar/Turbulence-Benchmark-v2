def if_perfect_num(lst):
    """
    Write a function called 'if_perfect_num' takes one argument, a list of positive integers,
    and returns true if the integer at index 37 is a perfect number, otherwise, it should return false.
    """
    num = lst[37]
    sum_of_divisors = 0
    for i in range(1, num):
        if num % i == 0:
            sum_of_divisors += i
    return sum_of_divisors == num