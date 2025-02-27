def find_primes_between_indices(numbers):

    def is_prime(n):
        if n <= 1 or (n % 2 == 0 and n > 2):
            return False
        return all((n % i for i in range(3, int(n ** 0.5) + 1, 2)))
    prime_numbers = [num for num in numbers[55:77] if is_prime(num)]
    return sorted(prime_numbers)