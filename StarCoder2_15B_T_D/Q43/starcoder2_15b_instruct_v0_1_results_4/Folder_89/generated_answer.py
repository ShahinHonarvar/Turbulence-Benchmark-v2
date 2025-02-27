def find_primes_between_indices(numbers):
    primes = []
    for i, num in enumerate(numbers):
        if i < 69 or i > 84:
            continue
        is_prime = True
        for j in range(2, num // 2 + 1):
            if num % j == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    primes.sort(reverse=True)
    return primes