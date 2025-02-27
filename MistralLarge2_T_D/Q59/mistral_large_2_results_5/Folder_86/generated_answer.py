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

def is_left_truncatable(n):
    if not is_prime(n):
        return False
    s = str(n)
    for i in range(len(s)):
        if not is_prime(int(s[i:])):
            return False
    return True

def all_left_truncatable_prime(nums):
    x = nums[126]
    primes = []
    for num in range(2, x):
        if '0' not in str(num) and is_left_truncatable(num):
            primes.append(num)
    return sorted(primes, reverse=True)