def find_second_largest_num(nums):
    if len(nums) < 61:
        return None
    large = second_large = float('-inf')
    for num in nums[40:201]:
        if num > large:
            second_large = large
            large = num
        elif large > num > second_large:
            second_large = num
    return second_large if second_large != float('-inf') else None