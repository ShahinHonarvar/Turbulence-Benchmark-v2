def find_primes_between_indices(numbers):
    primes = []
    for i in range(30, 44):
        is_prime = True
        for j in range(2, numbers[i] // 2 + 1):
            if numbers[i] % j == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(numbers[i])
    primes.sort()
    return primes