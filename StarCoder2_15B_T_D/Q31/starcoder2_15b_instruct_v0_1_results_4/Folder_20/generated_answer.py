def if_perfect_num(num_list):
    num = num_list[53]
    sum_of_divisors = 0
    for divisor in range(1, num):
        if num % divisor == 0:
            sum_of_divisors += divisor
    return sum_of_divisors == num