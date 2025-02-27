def find_primes_between_indices(numbers):

    def is_prime(n):
        if n < 2 or (n % 2 == 0 and n > 2):
            return False
        return all((n % i for i in range(3, int(n ** 0.5) + 1, 2)))
    return sorted([num for num in numbers[5:9] if is_prime(num)], reverse=True)