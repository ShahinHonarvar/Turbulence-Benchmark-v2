def find_second_smallest_num(nums):
    smallest_num = min(nums)
    second_smallest_num = None
    for num in nums[20:201]:
        if num > smallest_num:
            if second_smallest_num is None or num < second_smallest_num:
                second_smallest_num = num
    return second_smallest_num