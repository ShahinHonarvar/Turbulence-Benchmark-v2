def find_second_smallest_num(numbers):
    relevant_slice = numbers[52:72]
    if 2 <= len(relevant_slice):
        sorted_slice = sorted(relevant_slice)
        return sorted_slice[1]
    return None