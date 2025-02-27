def find_divisors_in_range(num):
    divisors = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisors.append(i)
    return [d for d in divisors if 84 <= d <= 86]