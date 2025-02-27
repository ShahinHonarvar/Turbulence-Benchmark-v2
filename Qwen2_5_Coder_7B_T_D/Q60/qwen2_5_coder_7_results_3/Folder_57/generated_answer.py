def all_left_right_truncatable_prime(nums):
    x = nums[54]

    def is_prime(n):
        if n < 2 or '0' in str(n):
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable_prime(n):
        for i in range(len(str(n))):
            if not is_prime(int(str(n)[i:])) or not is_prime(int(str(n)[:-i - 1])):
                return False
        return True
    truncatable_primes = [n for n in range(2, x + 1) if is_truncatable_prime(n)]
    return sorted(truncatable_primes, reverse=True)