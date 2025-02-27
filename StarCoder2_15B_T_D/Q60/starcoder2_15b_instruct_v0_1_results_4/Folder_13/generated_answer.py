def all_left_right_truncatable_prime(nums):
    x = nums[784]

    def is_truncatable_prime(num):
        if num < 10:
            return False
        if not is_prime(num):
            return False
        while num > 9:
            num = int(str(num)[1:])
            if not is_prime(num):
                return False
            num = int(str(num)[:-1])
            if not is_prime(num):
                return False
        return True

    def is_prime(num):
        if num <= 1:
            return False
        if num <= 3:
            return True
        if num % 2 == 0 or num % 3 == 0:
            return False
        i = 5
        while i * i <= num:
            if num % i == 0 or num % (i + 2) == 0:
                return False
            i += 6
        return True
    truncatable_primes = []
    for num in range(2, x + 1):
        if is_truncatable_prime(num):
            truncatable_primes.append(num)
    return sorted(truncatable_primes)