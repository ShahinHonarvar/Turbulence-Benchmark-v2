def find_primes_between_indices(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    start_index = 167
    end_index = 785
    prime_numbers = [n for n in numbers[start_index:end_index + 1] if is_prime(n)]
    prime_numbers.sort(reverse=True)
    return prime_numbers