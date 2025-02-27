def all_left_right_truncatable_prime(nums):

    def is_left_right_truncatable(n):
        s = str(n)
        while len(s) > 1:
            if s[0] == '0' or s[-1] == '0' or (not is_prime(int(s))):
                return False
            s = s[1:]
        return True

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = nums[98]
    left_right_truncatable_primes = []
    for i in range(2, x + 1):
        if is_left_right_truncatable(i):
            left_right_truncatable_primes.append(i)
    left_right_truncatable_primes.sort()
    return left_right_truncatable_primes