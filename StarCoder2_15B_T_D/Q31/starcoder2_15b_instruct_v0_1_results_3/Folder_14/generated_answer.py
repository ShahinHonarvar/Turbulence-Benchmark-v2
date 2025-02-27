def if_perfect_num(num_list):
    num = num_list[17]
    sum_divisors = 0
    for i in range(1, num + 1):
        if num % i == 0:
            sum_divisors += i
    return sum_divisors == num