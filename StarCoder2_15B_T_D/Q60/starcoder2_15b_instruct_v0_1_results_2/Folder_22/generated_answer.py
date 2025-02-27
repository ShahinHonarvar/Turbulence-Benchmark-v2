def is_truncatable_prime(num):
    num_str = str(num)
    for i in range(len(num_str)):
        if not is_prime(int(num_str[i:])):
            return False
        if not is_prime(int(num_str[:len(num_str) - i])):
            return False
    return True

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(nums):
    truncatable_primes = []
    for num in nums:
        if is_truncatable_prime(num):
            truncatable_primes.append(num)
    return sorted(truncatable_primes)