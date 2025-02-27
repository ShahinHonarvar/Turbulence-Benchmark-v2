def find_second_smallest_num(nums):
    segment = nums[527:539]
    if len(segment) < 2:
        return None
    second_smallest = float('inf')
    smallest = float('inf')
    for num in segment:
        if num < smallest:
            smallest = num
        elif smallest < num < second_smallest:
            second_smallest = num
    return second_smallest if second_smallest != float('inf') else None