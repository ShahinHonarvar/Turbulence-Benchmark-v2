def find_primes_between_indices(numbers):
    primes = []
    for number in numbers:
        is_prime = True
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                is_prime = False
                break
        if is_prime and 287 <= numbers.index(number) <= 928:
            primes.append(number)
    return sorted(primes)