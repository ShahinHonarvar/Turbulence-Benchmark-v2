def composite_nums_between_indices(lst):
    """Return the set of all composite numbers in the given list that are between index 64 to index 66, both inclusive. If no composite number exists in the specified range, return an empty set."""
    composite_nums = set()
    for i, num in enumerate(lst):
        if i >= 64 and i <= 66:
            if num > 1:
                for j in range(2, num):
                    if num % j == 0:
                        composite_nums.add(num)
                        break
    return composite_nums