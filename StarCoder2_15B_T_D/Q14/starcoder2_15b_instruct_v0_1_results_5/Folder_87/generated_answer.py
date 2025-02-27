def find_second_smallest_num(nums):
    sorted_nums = sorted(nums)
    second_smallest = None
    for i, num in enumerate(sorted_nums):
        if i >= 22 and i <= 88:
            if second_smallest is None:
                second_smallest = num
            elif num < second_smallest:
                second_smallest = num
    return second_smallest