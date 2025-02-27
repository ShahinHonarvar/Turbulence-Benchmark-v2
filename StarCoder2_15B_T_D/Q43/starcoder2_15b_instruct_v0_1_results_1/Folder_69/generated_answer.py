def find_primes_between_indices(numbers):
    primes = []
    for i in range(497, 931):
        number = numbers[i]
        is_prime = True
        for j in range(2, int(number ** 0.5) + 1):
            if number % j == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(number)
    return sorted(primes, reverse=True)