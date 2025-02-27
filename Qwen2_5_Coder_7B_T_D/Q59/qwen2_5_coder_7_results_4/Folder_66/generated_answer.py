def all_left_truncatable_prime(nums):
    x = nums[25]
    primes = [2, 3, 5, 7]
    result = []

    def is_prime(n):
        if n < 2:
            return False
        if n in primes:
            return True
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        primes.append(n)
        return True

    def is_left_truncatable(n):
        str_n = str(n)
        for i in range(len(str_n)):
            if not is_prime(int(str_n[i:])):
                return False
        return True
    for num in range(11, x):
        if is_prime(num) and is_left_truncatable(num) and ('0' not in str(num)):
            result.append(num)
    return sorted(result, reverse=True)