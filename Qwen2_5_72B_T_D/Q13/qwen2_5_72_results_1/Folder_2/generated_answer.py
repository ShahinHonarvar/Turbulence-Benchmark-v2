def find_second_largest_num(numbers):
    if len(numbers) < 40:
        return None
    sublist = numbers[15:40]
    if len(set(sublist)) < 2:
        return None
    largest = max(sublist)
    sublist.remove(largest)
    while largest in sublist:
        sublist.remove(largest)
    if not sublist:
        return None
    return max(sublist)