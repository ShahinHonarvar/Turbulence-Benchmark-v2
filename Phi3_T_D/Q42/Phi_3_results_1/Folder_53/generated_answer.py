def prime_factors(nums):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    if len(nums) < 74:
        return set()
    prime_factors_set = set()
    num = nums[73]
    for i in range(2, num + 1):
        while num % i == 0:
            if is_prime(i):
                prime_factors_set.add(i)
            num //= i
    return prime_factors_set