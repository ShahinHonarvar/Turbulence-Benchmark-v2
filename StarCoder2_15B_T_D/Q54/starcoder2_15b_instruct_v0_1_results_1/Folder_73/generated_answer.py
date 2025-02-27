def all_right_truncatable_prime(nums):
    x = nums[97]
    truncatable_primes = []
    for i in range(2, x):
        is_truncatable_prime = True
        for j in range(len(str(i)) - 1):
            truncated_num = int(str(i)[:-(j + 1)])
            if not is_prime(truncated_num):
                is_truncatable_prime = False
                break
        if is_truncatable_prime:
            truncatable_primes.append(i)
    truncatable_primes.sort()
    return truncatable_primes

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True