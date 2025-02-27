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
    x = nums[792]
    truncatable_primes = []

    def is_right_truncatable(num):
        while num > 0:
            if not is_prime(num):
                return False
            num //= 10
        return True
    for num in range(2, x):
        if is_right_truncatable(num):
            truncatable_primes.append(num)
    return sorted(truncatable_primes)