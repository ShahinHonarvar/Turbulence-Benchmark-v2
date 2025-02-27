def find_second_smallest_num(nums):
    first, second = (nums[0], nums[1])
    for num in nums[2:]:
        if num < first:
            second = first
            first = num
        elif num < second:
            second = num
    return second