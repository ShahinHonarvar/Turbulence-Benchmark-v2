def find_second_smallest_num(nums):
    sliced_nums = nums[75:95]
    if len(sliced_nums) < 2:
        return None
    smallest = second_smallest = float('inf')
    for num in sliced_nums:
        if num < smallest:
            second_smallest, smallest = (smallest, num)
        elif smallest < num < second_smallest:
            second_smallest = num
    return second_smallest if second_smallest != float('inf') else None