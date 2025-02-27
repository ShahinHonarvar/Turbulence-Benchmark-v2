def find_primes_between_indices(numbers):

    def is_prime(num):
        if num == 2:
            return True
        if num < 2 or num % 2 == 0:
            return False
        for i in range(3, int(num ** 0.5) + 1, 2):
            if num % i == 0:
                return False
        return True
    start_index = 23
    end_index = 39
    return sorted([num for i, num in enumerate(numbers) if is_prime(num) and start_index <= i <= end_index])