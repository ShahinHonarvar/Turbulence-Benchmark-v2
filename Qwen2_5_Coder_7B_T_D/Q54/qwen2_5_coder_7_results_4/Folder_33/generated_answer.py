def all_right_truncatable_prime(numbers):
    x = numbers[945]
    primes = [2, 3, 5, 7]
    right_truncatable_primes = []

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def add_digit(digit):
        nonlocal primes
        new_primes = []
        for prime in primes:
            new_number = prime * 10 + digit
            if is_prime(new_number):
                new_primes.append(new_number)
        primes += new_primes
    for digit in range(2, 10):
        add_digit(digit)
    for prime in primes:
        temp = prime
        while temp >= x:
            temp //= 10
        if temp == 0:
            right_truncatable_primes.append(prime)
    return sorted(right_truncatable_primes, reverse=True)