def sum_of_divisors_in_range(n):
    sum = 0
    for i in range(2, n):
        if n % i == 0 and 33 <= i <= 57:
            sum += i
    return sum if sum > 0 else 0