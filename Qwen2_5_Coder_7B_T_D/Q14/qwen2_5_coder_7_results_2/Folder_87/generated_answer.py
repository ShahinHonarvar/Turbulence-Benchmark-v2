def find_second_smallest_num(nums):
    subset = nums[22:89]
    if len(subset) < 2:
        return None
    smallest = second_smallest = float('inf')
    for num in subset:
        if num <= smallest:
            smallest, second_smallest = (num, smallest)
        elif num < second_smallest:
            second_smallest = num
    return second_smallest if second_smallest != float('inf') else None