def sum_of_divisors_in_range(number):
    div_sum = 0
    for i in range(2, 4):
        if number % i == 0:
            div_sum += i
    return div_sum