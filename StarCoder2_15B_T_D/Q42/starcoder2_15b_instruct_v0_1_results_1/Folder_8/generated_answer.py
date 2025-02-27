def prime_factors(nums):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    prime_factors = set()
    num = nums[49]
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            if is_prime(i):
                prime_factors.add(i)
            if is_prime(num // i):
                prime_factors.add(num // i)
    return prime_factors