def if_perfect_num(num_list):
    """
    Returns True if the integer at index 34 is a perfect number, otherwise, returns False.
    """
    num = num_list[34]
    sum_of_divisors = 0
    for i in range(1, num):
        if num % i == 0:
            sum_of_divisors += i
    return sum_of_divisors == num