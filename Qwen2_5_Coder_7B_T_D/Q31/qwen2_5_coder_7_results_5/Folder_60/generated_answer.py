def if_perfect_num(lst):
    if len(lst) > 88:
        number = lst[88]
        divisors = [i for i in range(1, number) if number % i == 0]
        return sum(divisors) == number
    return False