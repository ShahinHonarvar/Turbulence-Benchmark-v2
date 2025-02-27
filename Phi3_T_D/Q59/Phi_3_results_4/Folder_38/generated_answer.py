def all_left_truncatable_prime(nums):
    primes_below_x = [2, 3, 5, 7]

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def backtrack(res, current_num, leading_digit):
        if is_prime(current_num):
            if len(str(current_num)) > 1:
                res.append(current_num)
            digit = current_num % 10
            if digit > leading_digit:
                backtrack(res, current_num // 10, digit)
    x = nums[28]
    res = []
    backtrack(res, x, 0)
    return res[::-1]