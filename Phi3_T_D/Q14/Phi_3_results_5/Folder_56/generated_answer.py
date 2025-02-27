def find_second_smallest_num(nums):
    if len(nums) < 2:
        return None
    smallest = min(nums[:2])
    return min([num for num in nums if num > smallest])