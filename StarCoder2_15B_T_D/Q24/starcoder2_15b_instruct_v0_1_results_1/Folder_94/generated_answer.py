def sum_of_divisors_in_range(num):
    sum = 0
    for i in range(1, num + 1):
        if num % i == 0 and 35 <= i <= 37:
            sum += i
    return sum