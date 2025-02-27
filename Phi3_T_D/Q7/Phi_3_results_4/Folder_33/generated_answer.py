def all_even_ints_inclusive(arr):
    start_index, end_index = (667, 774)
    return [x for x in arr[start_index:end_index + 1] if x % 2 == 0]