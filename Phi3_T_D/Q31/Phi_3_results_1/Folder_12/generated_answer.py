def if_perfect_num(lst):
    if 27 < len(lst):
        num = lst[27]
        divisors = [i for i in range(1, num) if num % i == 0]
        return sum(divisors) == num
    else:
        return False