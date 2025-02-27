def find_second_smallest_num(nums):
    sliced_nums = nums[40:81]
    if len(sliced_nums) < 2:
        return None
    first = second = float('inf')
    for num in sliced_nums:
        if num <= first:
            first, second = (num, first)
        elif num < second:
            second = num
    return second if second != float('inf') else None