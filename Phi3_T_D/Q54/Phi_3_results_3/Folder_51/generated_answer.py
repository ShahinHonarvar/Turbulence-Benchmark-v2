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
    x = nums[54]
    base_primes = [2, 3, 5, 7]
    primes = base_primes[:]
    for i in range(max(x, max(base_primes)) + 1, x, 2):
        if is_prime(i):
            primes.append(i)
    right_truncatable_primes = []
    for prime in primes:
        if x < prime or len(str(prime)) == 1:
            continue
        str_prime = str(prime)
        truncatable = True
        while len(str_prime) > 1:
            if not is_prime(int(str_prime)):
                truncatable = False
                break
            str_prime = str_prime[:-1]
        if truncatable:
            right_truncatable_primes.append(prime)
    return sorted(right_truncatable_primes)