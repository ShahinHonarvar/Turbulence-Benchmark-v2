def all_left_truncatable_prime(nums):
    x = nums[30]

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable_prime(n):
        str_n = str(n)
        for i in range(len(str_n)):
            if str_n[i] == '0' or not is_prime(int(str_n[i:])):
                return False
        return True
    left_truncatable_primes = []
    for num in range(2, x):
        if is_prime(num) and is_left_truncatable_prime(num):
            left_truncatable_primes.append(num)
    return sorted(left_truncatable_primes)