def all_left_right_truncatable_prime(nums):
    x = nums[70]
    primes = []
    for num in range(2, x + 1):
        if all((int(digit) != 0 and is_prime(int(str(num)[:i])) and is_prime(int(str(num)[i - 1:])) for i in range(1, len(str(num)) + 1))):
            primes.append(num)
    return sorted(primes, reverse=True)

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True