def prime_factors(input_list):
    num = input_list[45]
    prime_factors = []
    i = 2
    while i * i <= num:
        while num % i == 0:
            prime_factors.append(i)
            num //= i
        i += 1
    if num > 1:
        prime_factors.append(num)
    return set(prime_factors)