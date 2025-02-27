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
    x = nums[55]
    primes = []
    for n in range(2, x):
        if is_prime(n):
            num = n
            while num > 0:
                if not is_prime(num):
                    break
                num //= 10
            else:
                primes.append(n)
    return sorted(primes, reverse=True)