def find_second_smallest_num(numbers):
    start_index = min(len(numbers), 52)
    end_index = min(len(numbers), 71) + 1
    slice_ = sorted(numbers[start_index:end_index])
    return slice_[1] if len(slice_) > 1 else None