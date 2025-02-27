def all_left_right_truncatable_prime(nums):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = nums[7]
    lr_trunc_primes = []
    for num in range(11, x + 1):
        if '0' not in str(num):
            n = num
            while n > 0 and is_prime(n):
                n = int(str(n)[1:-1])
            if n in [2, 3, 5, 7] or n == 0:
                lr_trunc_primes.append(num)
    return sorted(lr_trunc_primes)