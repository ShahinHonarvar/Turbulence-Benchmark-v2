def all_neg_ints_exclusive(nums):
    if not isinstance(nums, list) or not all((isinstance(n, int) for n in nums)):
        return []
    result = []
    for i, num in enumerate(nums):
        if num < 0 and 389 < i < 748:
            result.append(num)
    return result