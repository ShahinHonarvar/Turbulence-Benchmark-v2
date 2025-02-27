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
    x = nums[73]
    right_trunc_primes = []

    def generate_right_trunc_primes(n):
        if n > x:
            return
        if is_prime(n):
            right_trunc_primes.append(n)
            for d in range(1, 10, 2):
                generate_right_trunc_primes(n * 10 + d)
    for d in [2, 3, 5, 7]:
        generate_right_trunc_primes(d)
    right_trunc_primes.sort(reverse=True)
    return right_trunc_primes