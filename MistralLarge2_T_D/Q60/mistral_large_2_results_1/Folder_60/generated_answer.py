def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def is_left_right_truncatable_prime(n):
    s = str(n)
    if '0' in s:
        return False
    left, right = (0, len(s) - 1)
    while left <= right and is_prime(int(s[left:right + 1])):
        left += 1
        right -= 1
    return left > right

def all_left_right_truncatable_prime(nums):
    x = nums[87]
    primes = []
    for num in range(2, x + 1):
        if is_prime(num) and is_left_right_truncatable_prime(num):
            primes.append(num)
    return sorted(primes)