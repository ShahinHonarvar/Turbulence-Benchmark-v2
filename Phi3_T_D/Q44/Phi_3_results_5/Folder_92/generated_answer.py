def composite_nums_between_indices(nums):

    def is_composite(n):
        if n < 4 or n % 2 == 0:
            return n > 2
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return True
        return False
    return {num for num in nums[1:2] if is_composite(num)}