def find_second_largest_num(numbers):
    if len(numbers) < 33:
        return None
    sublist = numbers[28:33]
    if len(set(sublist)) < 2:
        return None
    largest = max(sublist)
    sublist.remove(largest)
    while sublist and largest == max(sublist):
        sublist.remove(largest)
    if not sublist:
        return None
    return max(sublist)