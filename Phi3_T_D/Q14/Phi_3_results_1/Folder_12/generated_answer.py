def find_second_smallest_num(numbers):
    sliced = numbers[31:73]
    if len(sliced) < 2:
        return None
    sorted_slice = sorted(sliced)
    return sorted_slice[1]