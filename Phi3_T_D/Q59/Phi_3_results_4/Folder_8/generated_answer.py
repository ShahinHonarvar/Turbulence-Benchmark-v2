def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def all_left_truncatable_prime(nums):
    x = nums[41]
    truncatable_primes = []
    for num in range(x - 1, 1, -1):
        num_str = str(num)
        is_left_truncatable = True
        while len(num_str) > 1:
            num_str = num_str[1:]
            if not is_prime(int(num_str)):
                is_left_truncatable = False
                break
        if is_left_truncatable:
            truncatable_primes.append(num)
    return truncatable_primes