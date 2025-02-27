def find_second_smallest_num(nums):
    start, end = (91, 99)
    second_min = None
    for i in range(start, end + 1):
        if second_min is None or nums[i] < second_min:
            second_min = nums[i]
        else:
            for j in range(i + 1, end + 1):
                if nums[j] != second_min and (second_min is None or nums[j] < second_min):
                    second_min = nums[j]
                    break
    return second_min