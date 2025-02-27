def find_primes_between_indices(numbers):
    primes = []
    for i, number in enumerate(numbers):
        if i < 38 or i > 55:
            continue
        is_prime = True
        for j in range(2, number):
            if number % j == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(number)
    primes.sort(reverse=True)
    return primes