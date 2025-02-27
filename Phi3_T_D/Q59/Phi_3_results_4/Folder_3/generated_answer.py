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
    x = nums[100]

    def is_left_truncatable_prime(number):
        for i in range(len(number)):
            if not is_prime(int(number[i:])):
                return False
        return True
    primes = [p for p in range(2, x) if is_left_truncatable_prime(str(p).zfill(len(str(x))))]
    return primes