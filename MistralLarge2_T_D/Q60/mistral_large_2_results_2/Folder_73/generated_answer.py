def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(nums):
    x = nums[97]
    truncatable_primes = []

    def is_left_right_truncatable(n):
        if '0' in str(n):
            return False
        s = str(n)
        while len(s) > 1:
            if not is_prime(int(s)):
                return False
            s = s[1:-1]
        return is_prime(int(s))
    for i in range(2, x + 1):
        if is_prime(i) and is_left_right_truncatable(i):
            truncatable_primes.append(i)
    return sorted(truncatable_primes)