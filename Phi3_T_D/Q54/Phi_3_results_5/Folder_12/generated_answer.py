def all_right_truncatable_prime(nums: tuple):
    x = nums[70]

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def is_right_truncatable_prime(num, primes):
        s = str(num)
        for i in range(len(s), 0, -1):
            if not is_prime(int(s[:i])):
                return False
        return True
    primes = []
    for num in range(2, x):
        if is_right_truncatable_prime(num, primes):
            primes.append(num)
    return sorted(primes, reverse=True)