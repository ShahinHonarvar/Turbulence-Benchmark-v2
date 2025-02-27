def gcf_two_nums(nums):
    if len(nums) > 90:
        gcf = nums[90]
        for i in range(90, 84, -1):
            gcf = nums[i - 1]
            for j in range(2, min(nums[i - 1], gcf) + 1):
                if nums[i - 1] % j == 0 and gcf % j == 0:
                    gcf = j
                    break
        return gcf
    else:
        raise IndexError('List index out of range')