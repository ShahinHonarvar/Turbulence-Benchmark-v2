def find_second_largest_num(numbers):
    if len(numbers) < 89:
        return None
    sublist = numbers[75:89]
    if len(set(sublist)) < 2:
        return None
    max_num = max(sublist)
    while max_num in sublist:
        sublist.remove(max_num)
    return max(sublist)