def all_left_truncatable_prime(nums):
    x = nums[7]
    primes = [2, 3, 5, 7]
    left_truncatable_primes = []

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    for num in range(11, x):
        num_str = str(num)
        if '0' in num_str:
            continue
        if all((is_prime(int(num_str[:i])) for i in range(1, len(num_str) + 1))):
            primes.append(num)
            left_truncatable_primes.append(num)
    return sorted(left_truncatable_primes)