def all_left_right_truncatable_prime(nums):
    x = nums[758]
    primes = []
    for num in range(2, x + 1):
        if is_prime(num) and is_left_right_truncatable(num):
            primes.append(num)
    return sorted(primes)

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

def is_left_right_truncatable(n):
    str_n = str(n)
    for i in range(len(str_n)):
        if '0' in str_n[i:]:
            return False
        if not is_prime(int(str_n[:i + 1])):
            return False
        if not is_prime(int(str_n[i:])):
            return False
    return True