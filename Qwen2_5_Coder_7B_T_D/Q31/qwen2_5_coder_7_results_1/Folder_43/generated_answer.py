def if_perfect_num(lst):
    if len(lst) > 29:
        num = lst[29]
        divisors = sum((i for i in range(1, num) if num % i == 0))
        return divisors == num
    return False