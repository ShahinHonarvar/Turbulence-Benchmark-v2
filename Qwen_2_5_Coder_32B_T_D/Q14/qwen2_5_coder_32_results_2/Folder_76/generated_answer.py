def find_second_smallest_num(nums):
    if len(nums) < 606:
        return None
    sublist = nums[533:606]
    try:
        first, second = (float('inf'), float('inf'))
        for num in sublist:
            if num < first:
                first, second = (num, first)
            elif first < num < second:
                second = num
        return second if second != float('inf') else None
    except:
        return None