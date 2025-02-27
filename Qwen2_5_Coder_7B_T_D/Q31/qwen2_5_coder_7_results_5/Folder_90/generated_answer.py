def if_perfect_num(lst):
    if len(lst) > 263:
        number = lst[263]
        sum_of_divisors = sum([i for i in range(1, number) if number % i == 0])
        return sum_of_divisors == number
    return False