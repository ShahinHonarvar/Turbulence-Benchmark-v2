def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(nums):
    x = nums[89]
    truncatable_primes = []

    def is_truncatable(num):
        n = num
        while n:
            if not is_prime(n):
                return False
            n = n % 10 ** len(str(num)) // 10
        return True
    for num in range(2, x + 1):
        if is_prime(num) and is_truncatable(num):
            truncatable_primes.append(num)
    return sorted(truncatable_primes, reverse=True)