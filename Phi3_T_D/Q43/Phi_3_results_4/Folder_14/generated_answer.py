def find_primes_between_indices(numbers):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    prime_numbers = []
    for num in numbers[9:67]:
        if is_prime(num):
            prime_numbers.append(num)
    return prime_numbers