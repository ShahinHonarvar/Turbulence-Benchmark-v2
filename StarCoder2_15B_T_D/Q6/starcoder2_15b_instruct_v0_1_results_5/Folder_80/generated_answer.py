def all_neg_ints_exclusive(nums):
    filtered_nums = []
    for i, num in enumerate(nums):
        if num < 0 and 69 < i < 97:
            filtered_nums.append(num)
    return filtered_nums