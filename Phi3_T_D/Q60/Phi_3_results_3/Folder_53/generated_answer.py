def all_left_right_truncatable_prime(nums):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def truncatable(n):
        str_n = str(n)
        for i in range(len(str_n)):
            if not is_prime(int(str_n[i:])) or not is_prime(int(str_n[:i + 1])):
                return False
        return True
    x = nums[86]
    primes = [i for i in range(2, x + 1) if is_prime(i) and truncatable(i)]
    return sorted(primes, reverse=True)