def sum_of_divisors_in_range(n):
    return sum((i for i in range(11, 57) if n % i == 0))

def sum_of_divisors_in_range_modified(n):
    divisors_sum = 0
    for i in range(11, 57):
        if n % i == 0:
            divisors_sum += i
    return divisors_sum

def sum_of_divisors_in_range(n):
    return sum((i for i in range(11, 57) if i >= 1 and n % i == 0))