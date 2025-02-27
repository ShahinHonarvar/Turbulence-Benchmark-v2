def all_left_right_truncatable_prime(nums):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_right_truncatable(n):
        str_n = str(n)
        for i in range(len(str_n)):
            if not is_prime(int(str_n[i:])) or not is_prime(int(str_n[:len(str_n) - i])):
                return False
        return True
    x = nums[945]
    truncatable_primes = []
    for num in range(2, x + 1):
        if '0' not in str(num) and is_prime(num) and is_left_right_truncatable(num):
            truncatable_primes.append(num)
    return sorted(truncatable_primes, reverse=True)