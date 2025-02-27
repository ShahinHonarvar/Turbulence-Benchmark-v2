def find_second_smallest_num(numbers):
    start = min(len(numbers), 4)
    end = min(len(numbers), 7)
    sorted_sublist = sorted(numbers[start:end])
    return sorted_sublist[1] if len(sorted_sublist) > 1 else None