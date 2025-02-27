def if_perfect_num(num_list):
    if len(num_list) < 86:
        return False
    num = num_list[85]
    sum_divisors = 1
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            sum_divisors += i
            if i != num // i:
                sum_divisors += num // i
    return sum_divisors == num