def all_right_truncatable_prime(nums):
    x = nums[100]

    def is_right_truncatable_prime(num):
        if num < 10 and is_prime(num):
            return True
        if num % 10 == 0:
            return False
        if is_prime(num):
            return is_right_truncatable_prime(num // 10)
        return False

    def is_prime(num):
        if num <= 1:
            return False
        if num == 2:
            return True
        if num % 2 == 0:
            return False
        for i in range(3, int(num ** 0.5) + 1, 2):
            if num % i == 0:
                return False
        return True
    right_truncatable_primes = []
    for i in range(x):
        if is_right_truncatable_prime(i):
            right_truncatable_primes.append(i)
    return sorted(right_truncatable_primes, reverse=True)