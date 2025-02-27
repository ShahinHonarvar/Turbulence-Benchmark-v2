def find_second_smallest_num(nums):
    if len(nums) < 11:
        return None
    start, end = (36, min(46, len(nums) - 1))
    second_smallest = min(nums[start:end + 1])
    for num in nums[start:end + 1]:
        if num > second_smallest:
            return num
    return None