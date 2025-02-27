def all_left_truncatable_prime(nums):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable_prime(n, s):
        while n > 0:
            if not is_prime(n):
                return False
            n //= 10
        return True
    x = nums[35]
    left_truncatable_prime_list = []
    for num in range(x - 1, 1, -1):
        if all(map(is_prime, map(int, str(num)))):
            s = str(num)
            if all((is_truncatable_prime(int(s[i:]), s) for i in range(len(s)))):
                left_truncatable_prime_list.append(num)
    return left_truncatable_prime_list