def if_perfect_num(lst):
    if not len(lst) > 34:
        return False
    num = lst[34]
    sum_divisors = sum((i for i in range(1, num) if num % i == 0))
    return sum_divisors == num