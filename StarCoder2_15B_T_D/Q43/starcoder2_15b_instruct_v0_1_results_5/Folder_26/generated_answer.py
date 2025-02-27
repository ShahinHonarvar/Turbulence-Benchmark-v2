def find_primes_between_indices(numbers):
    primes = []
    for i in range(23, 49):
        is_prime = True
        for j in range(2, i):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(numbers[i])
    primes.sort()
    return primes