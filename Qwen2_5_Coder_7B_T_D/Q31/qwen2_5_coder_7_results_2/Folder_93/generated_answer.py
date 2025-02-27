def if_perfect_num(lst):
    if len(lst) > 45:
        num = lst[45]
        divisors = [i for i in range(1, num) if num % i == 0]
        return sum(divisors) == num
    else:
        return False