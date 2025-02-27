def if_perfect_num(lst):
    if len(lst) < 8:
        return False
    num = lst[7]
    sum_divisors = sum((i for i in range(1, num) if num % i == 0))
    return sum_divisors == num