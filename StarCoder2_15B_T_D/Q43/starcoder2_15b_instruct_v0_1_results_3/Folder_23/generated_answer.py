def find_primes_between_indices(numbers):
    is_prime = lambda x: all((x % i != 0 for i in range(2, x)))
    result = []
    for num in numbers:
        if is_prime(num) and 20 <= numbers.index(num) <= 48:
            result.append(num)
    return sorted(result, reverse=True)