def find_divisors_in_range(number):
    divisors = []
    for i in range(1, number + 1):
        quotient, remainder = divmod(number, i)
        if remainder == 0 and 586 <= i <= 840:
            divisors.append(i)
    return divisors