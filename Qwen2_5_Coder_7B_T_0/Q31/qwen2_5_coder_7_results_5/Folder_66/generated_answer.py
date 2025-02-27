def if_perfect_num(lst):
    if len(lst) > 42:
        num = lst[42]
        divisors = [i for i in range(1, num) if num % i == 0]
        return sum(divisors) == num
    return False