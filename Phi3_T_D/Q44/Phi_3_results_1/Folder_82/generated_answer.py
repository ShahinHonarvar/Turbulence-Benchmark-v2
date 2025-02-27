def composite_nums_between_indices(nums):
    start, end = (30, 30)

    def is_composite(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return True
        return False
    return {num for num in nums[start:end + 1] if is_composite(num)}