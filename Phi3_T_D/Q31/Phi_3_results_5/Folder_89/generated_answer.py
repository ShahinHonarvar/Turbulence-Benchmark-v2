def if_perfect_num(lst):
    try:
        num = lst[18]
        divisors_sum = sum([i for i in range(1, num // 2 + 1) if num % i == 0])
        return divisors_sum == num
    except (IndexError, ValueError):
        return False