def find_primes_between_indices(numbers):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    start_index = 261
    end_index = 459
    prime_numbers = []
    for i, number in enumerate(numbers):
        if is_prime(number) and start_index <= i <= end_index:
            prime_numbers.append(number)
    return sorted(prime_numbers)