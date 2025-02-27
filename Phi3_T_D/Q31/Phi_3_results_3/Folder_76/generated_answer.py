def is_perfect_num(num):
    """Check if a number is perfect."""
    sum_of_divisors = 0
    for i in range(1, num):
        if num % i == 0:
            sum_of_divisors += i
    return sum_of_divisors == num

def if_perfect_num(lst):
    """Check if the number at index 537 is a perfect number."""
    if len(lst) > 537:
        return is_perfect_num(lst[537])
    return False