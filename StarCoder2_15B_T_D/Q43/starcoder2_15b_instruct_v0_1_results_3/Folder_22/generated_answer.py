def find_primes_between_indices(numbers):
    primes = []
    for i in range(75, 86):
        number = numbers[i]
        is_prime = True
        for j in range(2, number):
            if number % j == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(number)
    return sorted(primes)