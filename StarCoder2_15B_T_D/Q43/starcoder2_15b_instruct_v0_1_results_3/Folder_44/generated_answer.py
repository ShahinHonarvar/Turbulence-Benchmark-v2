def find_primes_between_indices(numbers):
    start_index = 19
    end_index = 85
    numbers_in_range = numbers[start_index:end_index + 1]
    primes = []
    is_prime = [True] * len(numbers_in_range)
    for i in range(2, int(len(numbers_in_range) ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, len(numbers_in_range), i):
                is_prime[j] = False
    for i in range(2, len(numbers_in_range)):
        if is_prime[i]:
            primes.append(numbers_in_range[i])
    primes.sort(reverse=True)
    return primes