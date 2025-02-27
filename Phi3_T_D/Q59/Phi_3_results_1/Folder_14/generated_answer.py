def all_left_truncatable_prime(nums):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable(n):
        n_str = str(n)
        for i in range(len(n_str)):
            if not is_prime(int(n_str[i:])):
                return False
        return True
    max_num = nums[77]
    prime_list = [i for i in range(2, max_num) if is_prime(i)]
    left_truncatable_primes = [p for p in prime_list if is_left_truncatable(p)]
    return sorted(left_truncatable_primes, reverse=True)