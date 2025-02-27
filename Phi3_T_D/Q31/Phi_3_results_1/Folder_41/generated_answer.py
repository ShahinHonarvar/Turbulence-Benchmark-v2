def is_perfect_num(num):
    """Check if a number is perfect"""
    sum_divisors = sum([i for i in range(1, num) if num % i == 0])
    return sum_divisors == num

def if_perfect_num(lst):
    return is_perfect_num(lst[84]) if len(lst) > 84 else False