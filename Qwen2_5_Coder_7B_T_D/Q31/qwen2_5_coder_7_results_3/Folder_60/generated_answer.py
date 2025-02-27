def if_perfect_num(lst):
    if len(lst) > 88:
        number = lst[88]
        sum_of_divisors = sum([i for i in range(1, number) if number % i == 0])
        return sum_of_divisors == number
    else:
        return False