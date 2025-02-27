def all_right_truncatable_prime(nums):
    x = nums[70]
    right_truncatable_primes = []
    for num in range(2, x):
        is_right_truncatable_prime = True
        for digit in str(num)[::-1]:
            if not is_prime(int(digit)):
                is_right_truncatable_prime = False
                break
        if is_right_truncatable_prime:
            right_truncatable_primes.append(num)
    return sorted(right_truncatable_primes, reverse=True)

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True