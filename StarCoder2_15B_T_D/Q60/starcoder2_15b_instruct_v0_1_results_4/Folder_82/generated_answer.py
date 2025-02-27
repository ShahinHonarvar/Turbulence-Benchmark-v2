def all_left_right_truncatable_prime(nums):
    x = nums[69]
    truncatable_primes = []
    for i in range(2, x + 1):
        if is_prime(i) and is_left_right_truncatable_prime(i):
            truncatable_primes.append(i)
    truncatable_primes.sort(reverse=True)
    return truncatable_primes

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def is_left_right_truncatable_prime(num):
    num_str = str(num)
    if len(num_str) <= 2:
        return is_prime(num)
    if num_str[0] == '0' or num_str[-1] == '0':
        return False
    return is_left_right_truncatable_prime(int(num_str[1:])) and is_left_right_truncatable_prime(int(num_str[:-1]))