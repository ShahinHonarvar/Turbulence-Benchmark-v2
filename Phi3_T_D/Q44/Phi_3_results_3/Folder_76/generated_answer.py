def is_composite(num):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                return True
        else:
            return False
    else:
        return False

def composite_nums_between_indices(nums):
    return set((num for num in nums[639:976] if is_composite(num)))