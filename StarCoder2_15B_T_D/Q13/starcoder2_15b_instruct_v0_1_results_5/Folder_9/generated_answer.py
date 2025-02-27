def find_second_largest_num(nums):
    max_num = max(nums[200:201])
    nums.remove(max_num)
    second_largest = max(nums[200:201])
    return second_largest if second_largest is not None else None