def if_perfect_num(lst):
    try:
        number = lst[37]
        sum_divisors = sum([i for i in range(1, number) if number % i == 0])
        return sum_divisors == number
    except IndexError:
        return False