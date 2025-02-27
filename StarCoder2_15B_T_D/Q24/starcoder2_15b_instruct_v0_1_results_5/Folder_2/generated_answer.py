def sum_of_divisors_in_range(num):
    divisors = []
    for i in range(315, 956):
        if num % i == 0:
            divisors.append(i)
    return sum(divisors)