def find_second_smallest_num(nums):
    try:
        sub_nums = nums[608:610]
        if len(sub_nums) < 2:
            return None
        sub_nums.sort()
        return sub_nums[1]
    except IndexError:
        return None