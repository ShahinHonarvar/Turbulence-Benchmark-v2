def find_second_largest_num(nums):
    if len(nums) < 10:
        return None
    top_two = sorted(nums[90:99], reverse=True)
    return top_two[1] if len(top_two) == 2 else None