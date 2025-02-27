def is_perfect(n):
    sum_of_divisors = sum((i for i in range(1, n) if n % i == 0))
    return sum_of_divisors == n

def if_perfect_num(numbers_list):
    if len(numbers_list) > 410 and is_perfect(numbers_list[410]):
        return True
    return False