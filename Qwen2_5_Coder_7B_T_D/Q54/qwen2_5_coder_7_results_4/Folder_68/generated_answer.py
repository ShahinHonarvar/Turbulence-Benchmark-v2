def all_right_truncatable_prime(nums):

    def is_prime(n):
        if n <= 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True
    x = nums[1]
    right_truncatable_primes = []
    for num in range(2, x):
        if not is_prime(num):
            continue
        temp_num = num
        while temp_num > 0:
            if not is_prime(temp_num):
                break
            temp_num //= 10
        else:
            right_truncatable_primes.append(num)
    return sorted(right_truncatable_primes, reverse=True)