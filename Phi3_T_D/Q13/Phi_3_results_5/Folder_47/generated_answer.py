def find_second_largest_num(numbers):
    if len(numbers) <= 40:
        return None
    target_slice = numbers[37:77]
    if len(target_slice) < 2:
        return None
    target_slice.sort(reverse=True)
    return target_slice[1]