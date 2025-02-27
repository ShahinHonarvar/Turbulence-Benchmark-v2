def find_second_smallest_num(nums):
    start = 62
    end = 63
    if len(nums) > end and len(set(nums[start:end + 1])) >= 2:
        second_smallest = sorted(set(nums[start:end + 1]))[1]
        return second_smallest
    return None