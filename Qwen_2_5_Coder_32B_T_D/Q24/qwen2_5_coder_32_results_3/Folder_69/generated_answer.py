def sum_of_divisors_in_range(n):
    s = 0
    for i in range(658, 869):
        if n % i == 0:
            s += i
    return s