def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def all_right_truncatable_prime(nums):
    x = nums[79]
    primes = []
    for num in range(2, x):
        n = num
        while n > 0 and is_prime(n):
            n //= 10
        if n == 0 and is_prime(num):
            primes.append(num)
    return sorted(primes, reverse=True)