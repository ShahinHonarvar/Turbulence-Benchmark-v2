def is_prime(n):
    if n <= 1:
        return False
    if n == 2 or n == 3:
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
    x = nums[61]
    primes = []
    for num in range(2, x):
        str_num = str(num)
        if all((is_prime(int(str_num[:i])) for i in range(1, len(str_num) + 1))):
            primes.append(num)
    return sorted(primes)