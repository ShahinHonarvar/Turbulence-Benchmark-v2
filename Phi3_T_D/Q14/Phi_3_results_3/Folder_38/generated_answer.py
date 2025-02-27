def find_second_smallest_num(nums):
    start, end = (37, 51)
    if end >= len(nums):
        end = len(nums) - 1
    segment = sorted(nums[start:end + 1])
    if len(segment) < 2:
        return None
    return segment[1]