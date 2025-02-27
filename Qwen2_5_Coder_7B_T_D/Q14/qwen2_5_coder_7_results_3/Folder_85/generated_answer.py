def find_second_smallest_num(nums):
    if len(nums) < 7:
        return 'None'
    first, second = (float('inf'), float('inf'))
    for num in nums[:7]:
        if num <= first:
            first, second = (num, first)
        elif num < second:
            second = num
    return second if second != float('inf') else 'None'