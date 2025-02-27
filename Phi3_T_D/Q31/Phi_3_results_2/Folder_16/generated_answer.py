def if_perfect_num(lst):
    if 162 < len(lst):
        num = lst[162]
        divisors_sum = sum([i for i in range(1, num) if num % i == 0])
        return divisors_sum == num
    return False