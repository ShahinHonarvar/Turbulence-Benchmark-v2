def find_second_smallest_num(numbers):
    if len(numbers) < 7:
        return None
    slice_list = numbers[:7]
    smallest = min(slice_list)
    slice_list.remove(smallest)
    second_smallest = min(slice_list) if slice_list else None
    return second_smallest