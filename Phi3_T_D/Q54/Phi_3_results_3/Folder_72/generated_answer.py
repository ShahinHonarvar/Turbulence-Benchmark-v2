def all_right_truncatable_prime(nums):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_right_truncatable_prime(n, sieve):
        while n:
            if not sieve[n] or n == 2:
                return False
            n //= 10
        return True
    x = nums[31]
    sieve = [True] * (x + 1)
    for i in range(2, x + 1):
        if sieve[i]:
            for j in range(i * 10, x + 1, i):
                sieve[j] = False
    result = []
    for i in range(2 * 10 ** (len(str(x)) // 2), x, -1):
        if is_right_truncatable_prime(i, sieve):
            result.append(i)
    return result