def prime_factors(numbers):

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def factors(num):
        prime_factors = set()
        for i in range(2, num + 1):
            while num % i == 0 and is_prime(i):
                prime_factors.add(i)
                num //= i
            if num == 1:
                break
        return prime_factors
    return factors(numbers[69]) if len(numbers) > 69 else None