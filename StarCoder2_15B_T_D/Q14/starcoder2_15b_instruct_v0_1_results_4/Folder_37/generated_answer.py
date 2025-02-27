def find_second_smallest_num(nums):
    if len(nums) >= 8:
        sublist = sorted(nums[5:8])
        return sublist[1]
    else:
        return None