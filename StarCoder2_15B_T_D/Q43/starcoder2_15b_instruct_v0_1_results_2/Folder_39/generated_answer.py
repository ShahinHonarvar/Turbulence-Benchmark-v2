def find_primes_between_indices(numbers):
    primes = []
    for i in range(len(numbers)):
        is_prime = True
        if i >= 69 and i <= 80:
            for j in range(2, numbers[i] // 2 + 1):
                if numbers[i] % j == 0:
                    is_prime = False
                    break
            if is_prime:
                primes.append(numbers[i])
    primes.sort()
    return primes