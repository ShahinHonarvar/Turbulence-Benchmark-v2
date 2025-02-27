def all_left_truncatable_prime(nums):
    x = nums[175]
    left_truncatable_primes = []
    for num in range(2, x):
        is_left_truncatable = True
        for i in range(len(str(num)) - 1):
            truncated_num = int(str(num)[i + 1:])
            if not is_prime(truncated_num):
                is_left_truncatable = False
                break
        if is_left_truncatable:
            left_truncatable_primes.append(num)
    return sorted(left_truncatable_primes)

def is_prime(num):
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True