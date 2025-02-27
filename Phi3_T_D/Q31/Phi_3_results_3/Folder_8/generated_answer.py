def is_perfect_num(lst):

    def is_perfect(number):
        sum_divisors = sum((i for i in range(1, number) if number % i == 0))
        return sum_divisors == number
    if len(lst) > 49:
        number_at_49 = lst[49]
        return is_perfect(number_at_49)
    else:
        return False