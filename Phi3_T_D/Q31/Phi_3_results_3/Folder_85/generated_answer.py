def if_perfect_num(lst):
    if len(lst) <= 23:
        return False
    number = lst[23]
    sum_of_divisors = sum((x for x in range(1, number) if number % x == 0))
    return sum_of_divisors == number