def find_second_largest_num(numbers):
    if len(numbers) < 202:
        return None
    relevant_slice = numbers[20:201]
    if len(relevant_slice) == 0:
        return None
    largest = max(relevant_slice)
    relevant_slice.remove(largest)
    second_largest = max(relevant_slice)
    return second_largest