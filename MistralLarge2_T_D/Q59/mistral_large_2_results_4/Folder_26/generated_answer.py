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

def is_left_truncatable_prime(num):
    s = str(num)
    if '0' in s:
        return False
    while s:
        if not is_prime(int(s)):
            return False
        s = s[1:]
    return True

def all_left_truncatable_prime(nums):
    x = nums[81]
    primes = [num for num in range(2, x) if is_left_truncatable_prime(num)]
    primes.sort(reverse=True)
    return primes