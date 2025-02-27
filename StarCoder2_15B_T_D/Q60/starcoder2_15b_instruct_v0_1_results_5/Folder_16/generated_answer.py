def all_left_right_truncatable_prime(nums):
    x = nums[792]
    truncatable_primes = []
    for num in range(2, x + 1):
        is_truncatable = True
        for i in range(len(str(num)) - 1):
            left_trunc = int(str(num)[i:])
            right_trunc = int(str(num)[:len(str(num)) - i])
            if not (is_prime(left_trunc) and is_prime(right_trunc)):
                is_truncatable = False
                break
        if is_truncatable:
            truncatable_primes.append(num)
    return sorted(truncatable_primes)

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True