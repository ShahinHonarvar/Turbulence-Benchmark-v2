def all_left_right_truncatable_prime(nums):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_right_truncatable(n):
        num_str = str(n)
        for i in range(len(num_str)):
            if not is_prime(int(num_str[i:])):
                return False
            if not is_prime(int(num_str[:len(num_str) - i])):
                return False
        return True
    truncatable_primes = []
    for num in nums:
        if is_left_right_truncatable(num) and is_prime(num):
            truncatable_primes.append(num)
    return sorted(truncatable_primes, reverse=True)