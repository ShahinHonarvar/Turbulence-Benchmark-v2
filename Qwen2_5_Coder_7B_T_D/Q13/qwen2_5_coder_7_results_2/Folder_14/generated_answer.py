def find_second_largest_num(numbers):
    if len(numbers) < 8:
        return None
    sublist = numbers[5:8]
    if len(sublist) < 2:
        return None
    largest = max(sublist)
    sublist.remove(largest)
    return max(sublist)