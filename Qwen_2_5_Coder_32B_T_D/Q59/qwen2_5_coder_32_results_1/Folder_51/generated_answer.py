def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def all_left_truncatable_prime(nums):
    x = nums[54]
    left_truncatable_primes = []
    for num in range(2, x):
        s = str(num)
        if '0' not in s:
            is_left_truncatable = True
            for i in range(len(s)):
                if not is_prime(int(s[i:])):
                    is_left_truncatable = False
                    break
            if is_left_truncatable:
                left_truncatable_primes.append(int(s))
    return left_truncatable_primes