def if_perfect_num(lst):
    if len(lst) < 2:
        return False
    num = lst[1]
    divisors = []
    for i in range(1, num):
        if num % i == 0:
            divisors.append(i)
    return sum(divisors) == num