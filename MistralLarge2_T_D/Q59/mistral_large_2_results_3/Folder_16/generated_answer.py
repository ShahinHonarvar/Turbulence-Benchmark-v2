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

    def is_left_truncatable(num):
        while num > 0:
            if not is_prime(num):
                return False
            num = int(str(num)[1:])
        return True
    x = nums[792]
    primes = []
    for num in range(2, x):
        if '0' not in str(num) and is_left_truncatable(num):
            primes.append(num)
    return sorted(primes)