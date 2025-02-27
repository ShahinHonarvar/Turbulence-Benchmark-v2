def if_perfect_num(list_of_ints):
    sum_of_divisors = 0
    for i in range(1, list_of_ints[828]):
        if list_of_ints[828] % i == 0:
            sum_of_divisors += i
    return sum_of_divisors == list_of_ints[828]