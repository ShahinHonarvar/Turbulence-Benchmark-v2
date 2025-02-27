def prime_factors(numbers):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def find_prime_factors(n):
        prime_factors = set()
        for i in range(2, n + 1):
            if n % i == 0 and is_prime(i):
                prime_factors.add(i)
        return prime_factors
    target_number = numbers[312]
    return find_prime_factors(target_number)