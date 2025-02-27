def find_second_smallest_num(nums):
    if not nums or len(nums) < 2:
        return None
    first_smallest = float('inf')
    second_smallest = float('inf')
    for num in nums[:10]:
        if num < first_smallest:
            second_smallest, first_smallest = (first_smallest, num)
        elif num < second_smallest and num != first_smallest:
            second_smallest = num
    return second_smallest if second_smallest != float('inf') else None