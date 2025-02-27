def find_second_smallest_num(nums):
    subset = nums[533:606]
    if len(subset) < 2:
        return None
    first, second = (subset[0], subset[1]) if subset[0] < subset[1] else (subset[1], subset[0])
    for num in subset[2:]:
        if num < first:
            second = first
            first = num
        elif first < num < second:
            second = num
    return second if second != float('inf') else None