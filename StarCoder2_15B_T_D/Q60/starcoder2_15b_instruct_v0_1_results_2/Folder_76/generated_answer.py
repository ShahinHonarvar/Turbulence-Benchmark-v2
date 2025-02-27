def is_left_right_truncatable_prime(num):
    num_str = str(num)
    if len(num_str) <= 2:
        return False
    for i in range(len(num_str)):
        truncated_num = int(num_str[i + 1:])
        if truncated_num < 2 or not all((truncated_num % j for j in range(2, int(truncated_num ** 0.5) + 1))):
            return False
    for i in range(len(num_str) - 1, -1, -1):
        truncated_num = int(num_str[:i])
        if truncated_num < 2 or not all((truncated_num % j for j in range(2, int(truncated_num ** 0.5) + 1))):
            return False
    return True

def all_left_right_truncatable_prime(nums):
    left_right_truncatable_primes = []
    for num in nums:
        if is_left_right_truncatable_prime(num):
            left_right_truncatable_primes.append(num)
    return sorted(left_right_truncatable_primes, reverse=True)