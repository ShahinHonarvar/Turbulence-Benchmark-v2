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
    x = nums[89]
    primes = [i for i in range(2, x) if is_prime(i)]
    truncatable_primes = []
    while primes:
        prime = primes.pop()
        for i in range(1, len(str(prime))):
            if is_prime(int(str(prime)[:-i])):
                truncatable_primes.append(prime)
                break
    return sorted(truncatable_primes, reverse=True) if truncatable_primes else []