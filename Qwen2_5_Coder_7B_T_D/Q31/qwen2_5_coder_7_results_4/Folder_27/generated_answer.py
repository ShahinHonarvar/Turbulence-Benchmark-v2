def if_perfect_num(lst):
    if 56 < len(lst):
        num = lst[56]
        sum_of_divisors = sum((i for i in range(1, num) if num % i == 0))
        return sum_of_divisors == num
    return False