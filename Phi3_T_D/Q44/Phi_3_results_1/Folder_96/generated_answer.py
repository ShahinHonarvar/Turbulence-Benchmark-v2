def composite_nums_between_indices(nums):

    def is_composite(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return True
        return False
    start_index = 60
    end_index = 200
    composite_numbers = {x for x in nums[start_index:end_index + 1] if is_composite(x)}
    return composite_numbers