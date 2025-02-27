def prime_factors(numbers):
    prime_factors = set()
    for number in numbers:
        is_prime = True
        for i in range(2, number):
            if number % i == 0:
                is_prime = False
                break
        if is_prime:
            prime_factors.add(number)
    return prime_factors