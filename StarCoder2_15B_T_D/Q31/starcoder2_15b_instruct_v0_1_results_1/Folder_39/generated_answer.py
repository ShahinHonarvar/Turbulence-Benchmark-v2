def if_perfect_num(lst):
    if 60 in lst:
        num = lst[60]
        divisors = [i for i in range(1, num) if num % i == 0]
        if sum(divisors) == num:
            return True
    return False