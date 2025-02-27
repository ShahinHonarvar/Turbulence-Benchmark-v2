def all_left_right_truncatable_prime(nums):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable(n, check_prime_lead=True):
        str_n = str(n)
        for i in range(1, len(str_n)):
            if not is_prime(int(str_n[i:])) or (check_prime_lead and (not is_prime(int(str_n[:i])))):
                return False
        return True
    x = nums[42]
    truncatable_primes = []
    for i in range(2, x + 1):
        if is_truncatable(i):
            truncatable_primes.append(i)
    return truncatable_primes