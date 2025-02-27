def all_right_truncatable_prime(nums):
    x = nums[3]
    primes = [2, 3, 5, 7]
    right_truncatable_primes = []

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    for i in range(10, x):
        if is_prime(i):
            str_i = str(i)
            while str_i:
                if not is_prime(int(str_i)):
                    break
                str_i = str_i[:-1]
            else:
                right_truncatable_primes.append(i)
    return sorted(right_truncatable_primes, reverse=True)