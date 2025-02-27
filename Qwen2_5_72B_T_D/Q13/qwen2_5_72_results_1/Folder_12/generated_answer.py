def find_second_largest_num(numbers):
    sublist = numbers[14:65]
    if len(sublist) < 2:
        return None
    max_num = max(sublist)
    sublist.remove(max_num)
    second_largest = max(sublist) if sublist else None
    return second_largest