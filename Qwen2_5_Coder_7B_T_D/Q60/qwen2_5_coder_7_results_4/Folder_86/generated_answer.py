def all_left_right_truncatable_prime(nums):
    x = nums[126]
    primes = [2, 3, 5, 7]
    left_right_truncatable = []

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_right_truncatable(n):
        if '0' in str(n):
            return False
        str_n = str(n)
        while len(str_n) > 1:
            if not is_prime(int(str_n)):
                return False
            str_n = str_n[1:]
            str_n = str_n[:-1]
        return is_prime(int(str_n))
    for num in range(2, x + 1):
        if is_prime(num) and is_left_right_truncatable(num):
            left_right_truncatable.append(num)
    return left_right_truncatable