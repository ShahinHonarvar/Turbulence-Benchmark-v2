def find_second_largest_num(nums):
    nums = nums[:3]
    nums = list(filter(lambda x: isinstance(x, (int, float)), nums))
    if len(nums) < 2:
        return None
    nums.sort()
    return nums[-2]