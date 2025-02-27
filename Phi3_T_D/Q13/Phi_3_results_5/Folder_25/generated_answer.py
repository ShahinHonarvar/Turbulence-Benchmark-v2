def find_second_largest_num(numbers):
    relevant_slice = numbers[29:94]
    if len(set(relevant_slice)) < 2:
        return None
    return sorted(set(relevant_slice))[-2]