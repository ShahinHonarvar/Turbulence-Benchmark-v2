def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_truncatable_prime(num):
    num_str = str(num)
    if '0' in num_str:
        return False
    while len(num_str) > 1:
        if not is_prime(int(num_str)):
            return False
        num_str = num_str[1:-1]
    return is_prime(int(num_str))

def all_left_right_truncatable_prime(nums):
    x = nums[370]
    truncatable_primes = [i for i in range(2, x + 1) if is_truncatable_prime(i)]
    return sorted(truncatable_primes, reverse=True)