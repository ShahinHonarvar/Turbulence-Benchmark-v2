def all_left_truncatable_prime(nums):

    def is_prime(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        for i in range(5, int(n ** 0.5) + 1, 6):
            if n % i == 0 or n % (i + 2) == 0:
                return False
        return True

    def recursive_left_truncatable(n, primes):
        if not n or n < 0:
            return
        if is_prime(n):
            primes.append(n)
            for digit in str(n)[1:]:
                recursive_left_truncatable(int(digit), primes)
    x = nums[19]
    rightmost_digit = str(x)[-1]
    truncated_primes = []
    for digit in map(str, range(2, int(rightmost_digit) + 1)):
        recursive_left_truncatable(int(digit), truncated_primes)
    return truncated_primes