def all_right_truncatable_prime(nums):
    x = nums[29]
    right_truncatable_primes = []

    def is_prime(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True
    for num in range(2, x):
        str_num = str(num)
        is_right_truncatable = True
        for i in range(len(str_num) - 1, 0, -1):
            if not is_prime(int(str_num[:i])):
                is_right_truncatable = False
                break
        if is_right_truncatable and is_prime(num):
            right_truncatable_primes.append(num)
    return sorted(right_truncatable_primes, reverse=True)