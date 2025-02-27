def if_perfect_num(lst):
    if len(lst) < 9:
        return False
    num = lst[8]
    divisors_sum = sum((i for i in range(1, num) if num % i == 0))
    return divisors_sum == num