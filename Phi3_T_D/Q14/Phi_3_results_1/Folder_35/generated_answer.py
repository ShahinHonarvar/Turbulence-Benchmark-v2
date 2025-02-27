def find_second_smallest_num(numbers):
    index_start, index_end = (15, 39)
    numbers_subset = numbers[index_start:index_end + 1]
    if len(numbers_subset) < 2:
        return None
    numbers_subset.sort()
    return numbers_subset[1]