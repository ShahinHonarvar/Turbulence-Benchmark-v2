def find_second_smallest_num(nums):
    if len(nums) < 2 or len(nums) - len(nums[56:58]) < 2:
        return None
    start_slice = sorted(nums[56:58])
    if start_slice[0] != start_slice[1]:
        return start_slice[1]
    return None