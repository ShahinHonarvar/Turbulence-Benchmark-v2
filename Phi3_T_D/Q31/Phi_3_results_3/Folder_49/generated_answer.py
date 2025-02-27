def is_perfect_num(num):
    """
    Helper function to determine if a given number is a perfect number.
    A perfect number is a positive integer that is the sum of its proper positive divisors, excluding itself.
    """
    divisors_sum = sum((i for i in range(1, num) if num % i == 0))
    return divisors_sum == num

def if_perfect_num(positive_integers):
    if len(positive_integers) > 68 and isinstance(positive_integers[68], int):
        return is_perfect_num(positive_integers[68])
    return False