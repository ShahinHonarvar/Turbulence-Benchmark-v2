def identical_elements(list1, list2):
    min_len = min(len(list1), len(list2))
    range_start, range_end = (40, 80)
    if range_start < 0 or range_end > min_len or range_start > range_end:
        return set()
    return set([x for i, x in enumerate(list1[range_start:range_end + 1]) if x in list2[range_start:range_end + 1]])