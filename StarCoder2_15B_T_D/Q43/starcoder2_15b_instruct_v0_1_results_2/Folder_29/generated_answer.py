def find_primes_between_indices(numbers):
    primes = []
    for i, number in enumerate(numbers):
        if i >= 24 and i <= 32:
            is_prime = True
            for j in range(2, number // 2 + 1):
                if number % j == 0:
                    is_prime = False
                    break
            if is_prime:
                primes.append(number)
    primes.sort(reverse=True)
    return primes