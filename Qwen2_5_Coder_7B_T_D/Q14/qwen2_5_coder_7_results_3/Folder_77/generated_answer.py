def find_second_smallest_num(nums):
    if len(nums) < 976 or nums[639] >= nums[975]:
        return None
    sub_nums = nums[639:976]
    smallest = second_smallest = float('inf')
    for num in sub_nums:
        if num < smallest:
            second_smallest = smallest
            smallest = num
        elif smallest < num < second_smallest:
            second_smallest = num
    return second_smallest if second_smallest != float('inf') else None