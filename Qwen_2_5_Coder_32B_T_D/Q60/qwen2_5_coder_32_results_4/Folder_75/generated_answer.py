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

def all_left_right_truncatable_prime(nums):
    x = nums[41]
    if x < 23:
        return []
    truncatable_primes = []
    for num in range(23, x + 1):
        s = str(num)
        if '0' in s:
            continue
        left_right = True
        right_left = True
        for i in range(1, len(s)):
            if not is_prime(int(s[i:])) or not is_prime(int(s[:-i])):
                left_right = False
                break
        if left_right:
            truncatable_primes.append(num)
    return truncatable_primes