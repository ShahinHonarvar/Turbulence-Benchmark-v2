def find_second_smallest_num(nums):
    if len(nums[9:101]) < 2:
        return None
    second_smallest = min(sorted(nums[9:101])[1:2][0])
    return second_smallest