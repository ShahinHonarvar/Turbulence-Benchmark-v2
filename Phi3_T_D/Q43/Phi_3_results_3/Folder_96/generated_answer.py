def find_primes_between_indices(numbers):

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    start_index = 31
    end_index = 67
    prime_numbers = [num for i, num in enumerate(numbers) if is_prime(num) and start_index <= i <= end_index]
    return sorted(prime_numbers, reverse=True)