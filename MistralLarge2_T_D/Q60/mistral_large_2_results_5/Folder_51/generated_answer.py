def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_left_right_truncatable_prime(n):
    if not is_prime(n) or '0' in str(n):
        return False
    n_str = str(n)
    while len(n_str) > 1:
        n_str = n_str[1:-1]
        if not is_prime(int(n_str)) or '0' in n_str:
            return False
    return True

def all_left_right_truncatable_prime(nums):
    x = nums[54]
    truncatable_primes = []
    for num in range(2, x + 1):
        if is_left_right_truncatable_prime(num):
            truncatable_primes.append(num)
    return sorted(truncatable_primes)