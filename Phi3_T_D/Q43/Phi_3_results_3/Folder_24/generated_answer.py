def find_primes_between_indices(numbers):

    def is_prime(num):
        if num > 1:
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    return False
            return True
        return False
    return sorted((x for x in numbers[38:56] if is_prime(x)), reverse=True)