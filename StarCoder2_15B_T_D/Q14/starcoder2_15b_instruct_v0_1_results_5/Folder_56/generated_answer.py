def find_second_smallest_num(nums):
    smallest, second_smallest = (float('inf'), float('inf'))
    for num in nums:
        if num < smallest:
            smallest, second_smallest = (num, smallest)
        elif num > smallest and num < second_smallest:
            second_smallest = num
    return second_smallest if second_smallest < float('inf') else None