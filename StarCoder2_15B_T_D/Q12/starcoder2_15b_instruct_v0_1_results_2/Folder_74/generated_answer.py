def find_smallest_num(nums):
    if not nums or len(nums) < 89:
        return None
    sublist = nums[22:89]
    smallest = min(sublist)
    return smallest