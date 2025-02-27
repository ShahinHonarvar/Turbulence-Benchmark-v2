def all_left_truncatable_prime(nums):
    x = nums[7]
    primes = set()

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
    for num in range(2, x):
        if is_prime(num):
            str_num = str(num)
            if '0' not in str_num:
                is_left_truncatable = True
                for i in range(len(str_num)):
                    if not is_prime(int(str_num[i:])):
                        is_left_truncatable = False
                        break
                if is_left_truncatable:
                    primes.add(num)
    return sorted(primes)