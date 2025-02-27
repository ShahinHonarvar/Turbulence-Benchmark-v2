def all_left_right_truncatable_prime(nums):
    x = nums[33]
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
        s = str(n)
        for i in range(len(s)):
            if not is_prime(int(s[i:])) or not is_prime(int(s[:len(s) - i])):
                return False
        return True
    for num in range(11, x + 1):
        if is_prime(num) and '0' not in str(num):
            if is_left_right_truncatable(num):
                left_right_truncatable.append(num)
    return sorted(left_right_truncatable)