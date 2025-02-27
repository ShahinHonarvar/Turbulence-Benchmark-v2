def all_left_truncatable_prime(nums):

    def is_prime(n):
        if n <= 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True
    x = nums[43]
    left_truncatable_primes = []
    for num in range(2, x):
        num_str = str(num)
        if '0' in num_str:
            continue
        if all((is_prime(int(num_str[:i])) for i in range(1, len(num_str) + 1))):
            left_truncatable_primes.append(num)
    return sorted(left_truncatable_primes)