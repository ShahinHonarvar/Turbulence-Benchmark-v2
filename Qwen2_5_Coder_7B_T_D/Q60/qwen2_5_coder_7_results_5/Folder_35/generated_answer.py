def all_left_right_truncatable_prime(nums):
    x = nums[177]
    is_prime = lambda n: n > 1 and all((n % i != 0 for i in range(2, int(n ** 0.5) + 1)))
    valid_digits = {'1', '3', '7', '9'}
    lr_truncatable_primes = []

    def is_lr_truncatable_prime(n):
        str_n = str(n)
        for i in range(len(str_n)):
            if str_n[i] not in valid_digits or not is_prime(int(str_n[i:])):
                return False
        for i in range(len(str_n) - 1, 0, -1):
            if str_n[:i] not in valid_digits or not is_prime(int(str_n[:i])):
                return False
        return True
    for num in range(2, x + 1):
        if is_lr_truncatable_prime(num):
            lr_truncatable_primes.append(num)
    return sorted(lr_truncatable_primes)