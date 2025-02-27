def find_primes_between_indices(numbers):

    def is_prime(n):
        if n <= 1 or (n % 2 == 0 and n > 2):
            return False
        return all((n % d for d in range(3, int(n ** 0.5) + 1, 2)))
    start_index = 22
    end_index = 50
    primes_in_range = [num for num in numbers[start_index:end_index + 1] if is_prime(num)]
    return sorted(primes_in_range, reverse=True)