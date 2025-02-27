def find_primes_between_indices(numbers):
    start_index = 3
    end_index = 8
    selected_numbers = numbers[start_index:end_index + 1]

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    primes = [n for n in selected_numbers if is_prime(n)]
    primes.sort()
    return primes