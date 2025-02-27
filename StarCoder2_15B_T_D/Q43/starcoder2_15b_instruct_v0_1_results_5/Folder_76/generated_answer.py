def find_primes_between_indices(numbers):
    primes = []
    for i, number in enumerate(numbers):
        if i < 149 or i > 979:
            continue
        is_prime = True
        for j in range(2, number):
            if number % j == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(number)
    primes.sort()
    return primes