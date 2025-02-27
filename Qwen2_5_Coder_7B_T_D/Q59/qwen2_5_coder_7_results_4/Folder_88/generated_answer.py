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
    x = nums[93]
    primes = [2, 3, 5, 7]
    for num in range(11, x, 2):
        if all((is_prime(int(str(num)[:i + 1])) for i in range(len(str(num))))):
            primes.append(num)
    return sorted(primes)