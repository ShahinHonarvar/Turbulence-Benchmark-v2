def find_second_largest_num(numbers):
    index_start, index_end = (22, 88)
    if index_end > len(numbers) - 1:
        index_end = len(numbers) - 1
    section = numbers[index_start:index_end + 1]
    if len(section) < 2:
        return None
    section.sort()
    return section[-2]