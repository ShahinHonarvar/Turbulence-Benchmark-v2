def if_perfect_num(lst):
    if len(lst) > 33:
        num = lst[33]
        divisor_sum = sum({i for i in range(1, num) if num % i == 0})
        return divisor_sum == num
    return False