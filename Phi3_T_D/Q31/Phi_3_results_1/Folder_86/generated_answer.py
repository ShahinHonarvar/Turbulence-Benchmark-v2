def if_perfect_num(lst):
    if 194 < len(lst):
        num = lst[194]
        sum_divisors = sum((i for i in range(1, num) if num % i == 0))
        return sum_divisors == num
    return False