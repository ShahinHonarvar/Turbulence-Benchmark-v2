def all_left_truncatable_prime(nums):
    x = nums[85]
    primes = [2, 3, 5, 7]

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def left_truncatable(n):
        while n > 0:
            if str(n)[0] == '0' or not is_prime(n):
                return False
            n = n // 10
        return True
    for num in range(11, x):
        if '0' not in str(num) and is_prime(num) and left_truncatable(num):
            primes.append(num)
    return sorted(primes)