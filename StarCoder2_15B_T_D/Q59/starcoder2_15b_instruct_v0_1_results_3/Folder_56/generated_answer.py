def all_left_truncatable_prime(nums):
    x = nums[30]

    def is_truncatable_prime(num):
        if num < 2:
            return False
        if num == 2:
            return True
        if num % 2 == 0:
            return False
        for i in range(3, int(num ** 0.5) + 1, 2):
            if num % i == 0:
                return False
        return True
    truncatable_primes = []
    for i in range(10):
        for j in range(10):
            for k in range(10):
                for l in range(10):
                    num = i * 1000 + j * 100 + k * 10 + l
                    if is_truncatable_prime(num) and num < x:
                        truncatable_primes.append(num)
    return sorted(truncatable_primes)