def is_truncatable_prime(num):
    if num < 2:
        return False
    if num in (2, 3):
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    if '0' in str(num):
        return False
    while num > 9:
        num = int(str(num)[1:])
        if num < 2 or num % 2 == 0 or num % 3 == 0:
            return False
    return True

def all_left_right_truncatable_prime(nums):
    x = nums[89]
    truncatable_primes = []
    for num in range(2, x + 1):
        if is_truncatable_prime(num):
            truncatable_primes.append(num)
    truncatable_primes.sort(reverse=True)
    return truncatable_primes