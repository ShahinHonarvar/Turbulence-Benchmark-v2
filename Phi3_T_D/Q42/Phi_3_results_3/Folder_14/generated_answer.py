def prime_factors(positive_integers):
    prime_factors_set = set()
    number = positive_integers[17]
    while number % 2 == 0:
        prime_factors_set.add(2)
        number //= 2
    for i in range(3, int(number ** 0.5) + 1, 2):
        while number % i == 0:
            prime_factors_set.add(i)
            number //= i
    if number > 2:
        prime_factors_set.add(number)
    return prime_factors_set