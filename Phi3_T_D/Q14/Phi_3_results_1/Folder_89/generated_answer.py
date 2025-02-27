def find_second_smallest_num(nums):
    if len(nums) > 63 and all((isinstance(num, (int, float)) for num in nums[62:63])):
        return min(nums[62:63], key=lambda x: (x is not None, x))
    return None