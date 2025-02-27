def prime_factors(numbers):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def find_primes(number):
        primes = set()
        divisor = 2
        while number > 1:
            while number % divisor == 0 and is_prime(divisor):
                primes.add(divisor)
                number //= divisor
            divisor += 1
        return primes
    if len(numbers) < 7:
        raise ValueError('The list must contain at least 7 integers.')
    return find_primes(numbers[6])