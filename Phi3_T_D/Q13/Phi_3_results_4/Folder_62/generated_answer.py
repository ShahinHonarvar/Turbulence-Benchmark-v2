def find_second_largest_num(nums):
    start = max(0, 91)
    end = min(len(nums), 99) + 1
    sliced = sorted(nums[start:end], reverse=True)
    return sliced[1] if len(sliced) > 1 else None