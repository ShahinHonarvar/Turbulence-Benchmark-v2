def find_smallest_num(nums):
    if len(nums) > 200:
        return min(nums[30:201])
    try:
        return min(nums[max(0, len(nums) - 201):len(nums) - 29])
    except ValueError:
        return None