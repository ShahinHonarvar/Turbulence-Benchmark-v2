def all_odd_ints_inclusive(nums):
    odd_ints = []
    for num in nums:
        if num % 2 == 1:
            odd_ints.append(num)
    if not odd_ints:
        return []
    return odd_ints