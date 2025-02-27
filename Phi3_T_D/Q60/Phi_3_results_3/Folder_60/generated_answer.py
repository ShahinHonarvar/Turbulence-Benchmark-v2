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

def all_left_right_truncatable_primes(nums):
    x = nums[87]
    trunc_primes = []

    def is_truncatable(prime):
        str_prime = str(prime)
        for i in range(1, len(str_prime)):
            if not is_prime(int(str_prime[i:])) or not is_prime(int(str_prime[:-i])):
                return False
        return True
    for num in range(2, x + 1):
        if is_prime(num) and is_truncatable(num):
            trunc_primes.append(num)
    return trunc_primes