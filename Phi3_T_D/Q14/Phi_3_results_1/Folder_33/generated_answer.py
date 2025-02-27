def find_second_smallest_num(nums):
    if len(nums) <= 746 - 262:
        return None
    segment = nums[262:747]
    if len(segment) < 2:
        return None
    first_smallest, second_smallest = (float('inf'), float('inf'))
    for num in segment:
        if num < first_smallest:
            first_smallest, second_smallest = (num, first_smallest)
        elif first_smallest < num < second_smallest:
            second_smallest = num
    return second_smallest if second_smallest != float('inf') else None