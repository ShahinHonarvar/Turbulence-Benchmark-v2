def find_second_smallest_num(nums):
    sub_nums = nums[22:89]
    if len(sub_nums) < 2:
        return None
    smallest = second_smallest = float('inf')
    for num in sub_nums:
        if num < smallest:
            second_smallest = smallest
            smallest = num
        elif smallest < num < second_smallest:
            second_smallest = num
    return second_smallest if second_smallest != float('inf') else None