def is_perfect_num(num):
    """
    Check if a number is perfect.
    A perfect number is a positive integer that is equal to the sum of its proper positive divisors, excluding the number itself.
    """
    if num < 2:
        return False
    sum_of_divisors = 1
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            sum_of_divisors += i
            if i != num // i:
                sum_of_divisors += num // i
    return num == sum_of_divisors

def if_perfect_num(int_list):
    len_int_list = len(int_list)
    if len_int_list >= 829:
        return is_perfect_num(int_list[828])
    else:
        return False