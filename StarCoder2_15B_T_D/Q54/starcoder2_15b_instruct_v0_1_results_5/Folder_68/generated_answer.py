def all_right_truncatable_prime(nums):

    def is_right_truncatable_prime(n):
        if n < 2:
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
    result = []
    for i in range(2, x):
        j = i
        while j > 0:
            if is_right_truncatable_prime(j):
                result.append(j)
                break
            j //= 10
    result.sort(reverse=True)
    return result