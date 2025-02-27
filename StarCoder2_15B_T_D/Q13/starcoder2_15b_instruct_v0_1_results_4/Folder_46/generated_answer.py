def find_second_largest_num(list_of_nums):
    subset = list_of_nums[30:88]
    sorted_subset = sorted(subset, reverse=True)
    if len(sorted_subset) >= 2:
        return sorted_subset[1]
    else:
        return None