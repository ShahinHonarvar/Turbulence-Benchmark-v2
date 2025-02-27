def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(nums):
    x = nums[0]
    truncatable_primes = []
    for n in range(1, x + 1):
        if '0' in str(n):
            continue
        curr = n
        while curr >= 10:
            if not is_prime(curr):
                break
            curr //= 10
        else:
            curr = n
            while curr >= 10:
                if not is_prime(curr):
                    break
                curr %= 10 ** (len(str(curr)) - 1)
            else:
                truncatable_primes.append(n)
    return sorted(truncatable_primes)