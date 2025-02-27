def find_second_smallest_num(numbers):
    start_idx = min(12, len(numbers))
    end_idx = min(92, len(numbers))
    if end_idx - start_idx < 2:
        return None
    sorted_slice = sorted(numbers[start_idx:end_idx + 1])
    return sorted_slice[1] if sorted_slice else None