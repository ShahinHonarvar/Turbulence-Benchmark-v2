def composite_nums_between_indices(nums):

    def is_composite(num):
        for i in range(2, num):
            if num % i == 0:
                return True
        return False
    return {num for idx, num in enumerate(nums) if is_composite(num) and 56 <= idx <= 98}