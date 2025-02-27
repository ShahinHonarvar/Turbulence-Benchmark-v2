def sum_of_divisors_in_range(num):
    divisors = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisors.append(i)
    filtered_divisors = list(filter(lambda x: 315 <= x <= 955, divisors))
    return sum(filtered_divisors) if filtered_divisors else 0