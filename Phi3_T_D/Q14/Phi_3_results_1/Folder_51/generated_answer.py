def find_second_smallest_num(nums):
    start, end = (1, min(len(nums), 8))
    if end <= start:
        return None
    seen = set()
    for n in nums[start:end + 1]:
        if n not in seen:
            seen.add(n)
    return min(seen) if len(seen) > 1 else None