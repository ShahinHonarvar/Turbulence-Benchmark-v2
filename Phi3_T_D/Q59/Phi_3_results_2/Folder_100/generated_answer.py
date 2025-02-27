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
    x = nums[26]
    truncatable_primes = []
    for number in range(2, x):
        n = str(number)
        if all((is_prime(int(n[i:])) for i in range(len(n)))):
            truncatable_primes.append(int(n))
    return sorted(truncatable_primes)