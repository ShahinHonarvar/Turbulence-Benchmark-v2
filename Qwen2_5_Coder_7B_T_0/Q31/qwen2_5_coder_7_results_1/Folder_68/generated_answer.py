def if_perfect_num(lst):
    if len(lst) < 4:
        return False
    num = lst[3]
    divisors = [i for i in range(1, num) if num % i == 0]
    return sum(divisors) == num