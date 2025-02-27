def find_smallest_num(numbers):
    start_index = min(len(numbers), 84)
    end_index = min(len(numbers), 70)
    return min(numbers[start_index:end_index + 1])