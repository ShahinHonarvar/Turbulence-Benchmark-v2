def all_left_right_truncatable_prime(nums):
    x = nums[0]

    def is_prime(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    def is_truncatable_prime(n, prime_checker):
        str_n = str(n)
        return all((prime_checker(int(str_n[i:])) and prime_checker(int(str_n[:i + 1])) for i in range(len(str_n)))) if len(str_n) > 2 else prime_checker(n)
    return sorted((n for n in range(x, 11, -1) if is_truncatable_prime(n, is_prime))) if x in range(11, x) else []