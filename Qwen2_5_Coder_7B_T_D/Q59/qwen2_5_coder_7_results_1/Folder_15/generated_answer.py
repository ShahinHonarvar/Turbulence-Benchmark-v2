def all_left_truncatable_prime(nums):
    x = nums[6]
    primes = [2, 3, 5, 7]

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable(n):
        while n > 0:
            if str(n)[0] == '0' or not is_prime(n):
                return False
            n = int(str(n)[1:])
        return True
    result = []
    for i in range(11, x):
        if str(i).count('0') == 0 and is_prime(i) and is_left_truncatable(i):
            result.append(i)
    return sorted(result, reverse=True)