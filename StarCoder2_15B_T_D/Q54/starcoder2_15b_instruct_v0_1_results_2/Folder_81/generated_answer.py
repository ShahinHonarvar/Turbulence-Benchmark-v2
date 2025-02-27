def all_right_truncatable_prime(nums):
    right_truncatable_primes = []
    for num in nums:
        if num < 100:
            continue
        is_right_truncatable = True
        for i in range(len(str(num)) - 1, 0, -1):
            truncated_num = int(str(num)[:i])
            if not is_prime(truncated_num):
                is_right_truncatable = False
                break
        if is_right_truncatable:
            right_truncatable_primes.append(num)
    return sorted(right_truncatable_primes)

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True