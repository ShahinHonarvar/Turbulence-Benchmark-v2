def find_second_smallest_num(nums):
    sorted_nums = sorted(nums)
    second_smallest = None
    for i, num in enumerate(sorted_nums):
        if i >= 75 and i <= 88:
            if second_smallest is None:
                second_smallest = num
            else:
                return num
    return second_smallest