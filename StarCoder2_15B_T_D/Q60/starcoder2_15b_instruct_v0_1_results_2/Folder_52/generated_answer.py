def all_left_right_truncatable_prime(nums):
    x = nums[52]
    truncatable_primes = []
    for num in range(2, x + 1):
        is_truncatable = True
        for i in range(len(str(num)) - 1):
            truncated_num = int(str(num)[i + 1:])
            if not is_prime(truncated_num):
                is_truncatable = False
                break
            truncated_num = int(str(num)[:-i - 1])
            if not is_prime(truncated_num):
                is_truncatable = False
                break
        if is_truncatable:
            truncatable_primes.append(num)
    truncatable_primes.sort(reverse=True)
    return truncatable_primes

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True