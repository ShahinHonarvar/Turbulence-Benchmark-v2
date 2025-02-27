def sum_of_divisors_in_range(number):
    total = 0
    for i in range(1, number + 1):
        if number % i == 0 and 14 <= i <= 48:
            total += i
    return total