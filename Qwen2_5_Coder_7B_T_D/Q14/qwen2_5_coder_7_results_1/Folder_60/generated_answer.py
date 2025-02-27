def find_second_smallest_num(nums):
    if len(nums[56:99]) < 2:
        return None
    subset = nums[56:99]
    smallest = float('inf')
    second_smallest = float('inf')
    for num in subset:
        if num < smallest:
            second_smallest = smallest
            smallest = num
        elif smallest < num < second_smallest:
            second_smallest = num
    return second_smallest if second_smallest != float('inf') else None