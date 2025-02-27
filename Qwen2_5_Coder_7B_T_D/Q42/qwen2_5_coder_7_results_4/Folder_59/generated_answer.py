def prime_factors(numbers):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    if len(numbers) < 3:
        return set()
    target_number = numbers[2]
    prime_factors_set = set()
    for i in range(2, target_number + 1):
        while target_number % i == 0 and is_prime(i):
            prime_factors_set.add(i)
            target_number //= i
    return prime_factors_set