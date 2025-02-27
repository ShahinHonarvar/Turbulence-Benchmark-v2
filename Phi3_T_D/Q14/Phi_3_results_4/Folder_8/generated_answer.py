def find_second_smallest_num(numbers):
    relevant_slice = numbers[56:67]
    if len(relevant_slice) < 2:
        return None
    return sorted(relevant_slice)[1]