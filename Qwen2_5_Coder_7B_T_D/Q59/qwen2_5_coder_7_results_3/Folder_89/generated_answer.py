def all_left_truncatable_prime(nums):
    x = nums[97]
    limit = x - 1
    primes = [2, 3, 5, 7]
    left_truncatable_primes = []

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    for num in range(11, limit, 2):
        if all((is_prime(int(str(num)[:i])) for i in range(1, len(str(num)) + 1))) and '0' not in str(num):
            primes.append(num)
            left_truncatable_primes.append(num)
    return sorted(left_truncatable_primes, reverse=True)