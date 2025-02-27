def composite_nums_between_indices(nums):
    start, end = (21, 97)

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    composite_set = {num for num in nums[start:end + 1] if not is_prime(num)}
    return composite_set