def find_second_largest_num(numbers):
    if len(numbers) < 11:
        return None
    elems = set(numbers[10:101])
    max1 = max(elems)
    elems.remove(max1)
    max2 = max(elems) if elems else None
    return max2