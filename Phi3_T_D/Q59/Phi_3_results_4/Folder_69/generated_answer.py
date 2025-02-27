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
    x = nums[760]
    primes = [i for i in range(7, x) if is_prime(i)]
    result = []

    def check_left_truncatable(num):
        s = str(num)
        while len(s) > 1:
            if not is_prime(int(s)):
                return False
            s = s[1:]
        return True
    for prime in primes:
        if check_left_truncatable(prime):
            result.append(prime)
    return sorted(result, reverse=True)