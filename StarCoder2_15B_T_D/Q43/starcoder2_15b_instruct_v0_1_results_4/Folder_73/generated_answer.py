def find_primes_between_indices(numbers):
    prime_numbers = []
    if len(numbers) < 20:
        return prime_numbers
    for i in range(19, len(numbers)):
        is_prime = True
        for j in range(2, int(numbers[i] ** 0.5) + 1):
            if numbers[i] % j == 0:
                is_prime = False
                break
        if is_prime:
            prime_numbers.append(numbers[i])
    prime_numbers.sort(reverse=True)
    return prime_numbers