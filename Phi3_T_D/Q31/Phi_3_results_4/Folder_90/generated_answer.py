def if_perfect_num(lst):
    if len(lst) > 263:
        number_to_check = lst[263]
        divisors_sum = sum([i for i in range(1, number_to_check) if number_to_check % i == 0])
        return divisors_sum == number_to_check
    return False