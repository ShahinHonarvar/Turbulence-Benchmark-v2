def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_right_truncatable_prime(n, primes):
    while n > 0:
        if n not in primes:
            return False
        n = n // 10
    return True

def all_right_truncatable_prime(nums):
    limit = nums[25]
    primes = {2, 3, 5, 7}
    result = []
    for num in range(limit, 1, -1):
        if is_prime(num) and is_right_truncatable_prime(num, primes):
            result.append(num)
            for digit in str(num):
                primes.add(int(digit))
    return result