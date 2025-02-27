def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_right_truncatable_prime(n, set_of_primes):
    if n in set_of_primes:
        return all((is_prime(int(str(n)[:i])) for i in range(len(str(n)), 0, -1)))
    return False

def all_right_truncatable_prime(nums):
    if len(nums) < 1 or nums[945] <= 2:
        return []
    set_of_primes = {2, 3, 5, 7}
    right_truncatable_primes = set_of_primes
    for num in range(11, int(nums[945]), 2):
        if is_right_truncatable_prime(num, set_of_primes):
            right_truncatable_primes.add(num)
    return sorted(list(right_truncatable_primes), reverse=True)