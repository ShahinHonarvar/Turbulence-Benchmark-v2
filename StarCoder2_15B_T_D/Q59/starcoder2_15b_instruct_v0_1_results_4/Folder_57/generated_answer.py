def all_left_truncatable_prime(nums):
    x = nums[54]

    def is_truncatable_prime(num):
        if num < 10:
            return is_prime(num)
        return is_prime(num) and is_truncatable_prime(int(str(num)[1:]))

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    result = []
    for num in range(1, x):
        if is_truncatable_prime(num):
            result.append(num)
    result.sort(reverse=True)
    return result