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
    x = nums[65]
    primes = []
    n = 2
    while n < x:
        if is_prime(n) and (not any(map(lambda d: d == '0', str(n)))):
            s = str(n)
            while s:
                if not is_prime(int(s)):
                    break
                s = s[1:]
            else:
                primes.append(n)
        n += 1
    return sorted(primes, reverse=True)