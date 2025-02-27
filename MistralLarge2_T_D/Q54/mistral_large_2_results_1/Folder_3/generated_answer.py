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

def all_right_truncatable_prime(nums):
    x = nums[100]
    primes = []

    def is_right_truncatable_prime(n):
        s = str(n)
        for i in range(len(s)):
            if not is_prime(int(s[:len(s) - i])):
                return False
        return True
    for num in range(2, x):
        if is_right_truncatable_prime(num):
            primes.append(num)
    return sorted(primes)