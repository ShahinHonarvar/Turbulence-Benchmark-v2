def find_second_largest_num(numbers):
    relevant_slice = numbers[56:99]
    if len(relevant_slice) < 2:
        return None
    relevant_slice.sort(reverse=True)
    return relevant_slice[1] if relevant_slice[0] != relevant_slice[1] else None