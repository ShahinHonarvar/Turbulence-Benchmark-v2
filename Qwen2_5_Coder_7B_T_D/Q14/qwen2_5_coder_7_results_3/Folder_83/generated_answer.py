def find_second_smallest_num(nums):
    sliced_nums = nums[90:201]
    if len(sliced_nums) < 2:
        return None
    smallest = float('inf')
    second_smallest = float('inf')
    for num in sliced_nums:
        if num <= smallest:
            smallest, second_smallest = (num, smallest)
        elif num < second_smallest:
            second_smallest = num
    return second_smallest if second_smallest != float('inf') else None