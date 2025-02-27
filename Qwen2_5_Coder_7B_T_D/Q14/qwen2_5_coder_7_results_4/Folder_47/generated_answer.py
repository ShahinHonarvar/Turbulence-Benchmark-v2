def find_second_smallest_num(nums):
    lst = nums[22:64]
    if len(lst) < 2:
        return None
    smallest = second_smallest = float('inf')
    for num in lst:
        if num < smallest:
            smallest, second_smallest = (num, smallest)
        elif smallest < num < second_smallest:
            second_smallest = num
    return second_smallest if second_smallest != float('inf') else None