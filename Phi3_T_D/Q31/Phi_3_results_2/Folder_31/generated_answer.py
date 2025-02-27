def if_perfect_num(lst):
    if len(lst) > 66:
        divisors = [i for i in range(1, lst[66] // 2 + 1) if lst[66] % i == 0]
        return sum(divisors) == lst[66]
    return False