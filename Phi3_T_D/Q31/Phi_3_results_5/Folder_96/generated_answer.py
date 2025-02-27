def if_perfect_num(list_of_integers):
    if len(list_of_integers) < 48:
        return False

    def sum_divisors(n):
        return sum((i for i in range(1, n) if n % i == 0))
    target_index = 47
    target_value = list_of_integers[target_index]
    return target_value == sum_divisors(target_value)