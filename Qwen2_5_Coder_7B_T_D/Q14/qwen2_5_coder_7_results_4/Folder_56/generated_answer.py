def find_second_smallest_num(nums):
    if len(nums) < 2:
        return None
    smallest = second_smallest = float('inf')
    for num in nums:
        if num < smallest:
            smallest, second_smallest = (num, smallest)
        elif smallest < num < second_smallest:
            second_smallest = num
    return second_smallest if second_smallest != float('inf') else None