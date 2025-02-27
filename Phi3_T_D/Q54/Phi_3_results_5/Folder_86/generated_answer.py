def all_right_truncatable_prime(nums):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    right_truncatable_primes = []
    x = nums[126]

    def is_right_truncatable(n):
        if not is_prime(n):
            return False
        str_n = str(n)
        while str_n:
            if not is_prime(int(str_n)):
                return False
            str_n = str_n[:-1]
        return True
    for num in range(x - 1, 11, -1):
        if '0' in str(num):
            continue
        if is_right_truncatable(num):
            right_truncatable_primes.append(num)
        if not right_truncatable_primes:
            return []
    return right_truncatable_primes