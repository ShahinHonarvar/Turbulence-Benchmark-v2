def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def is_left_truncatable_prime(num):
    num_str = str(num)
    if '0' in num_str:
        return False
    for i in range(len(num_str)):
        if not is_prime(int(num_str[i:])):
            return False
    return True

def all_left_truncatable_prime(nums):
    x = nums[20]
    primes = [num for num in range(2, x) if is_left_truncatable_prime(num)]
    return sorted(primes, reverse=True)