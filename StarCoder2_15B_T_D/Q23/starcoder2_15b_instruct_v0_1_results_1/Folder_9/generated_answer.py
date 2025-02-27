def find_divisors_in_range(num):
    divisors = []
    for i in range(3, 10):
        quotient, remainder = divmod(num, i)
        if remainder == 0 and 3 <= quotient <= 9:
            divisors.append(i)
    return divisors