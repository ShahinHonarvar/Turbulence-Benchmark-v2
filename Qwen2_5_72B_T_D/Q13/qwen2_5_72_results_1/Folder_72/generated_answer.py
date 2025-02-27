def find_second_largest_num(numbers):
    sublist = numbers[29:52]
    if len(sublist) <= 1:
        return None
    max_num = max(sublist)
    sublist.remove(max_num)
    if not sublist:
        return None
    second_largest = max(sublist)
    return second_largest