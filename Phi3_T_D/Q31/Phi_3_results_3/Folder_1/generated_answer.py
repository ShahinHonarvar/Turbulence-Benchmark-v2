def if_perfect_num(lst):
    try:
        num = lst[85]
        divisors_sum = sum([i for i in range(1, num) if num % i == 0])
        return divisors_sum == num
    except IndexError:
        return False