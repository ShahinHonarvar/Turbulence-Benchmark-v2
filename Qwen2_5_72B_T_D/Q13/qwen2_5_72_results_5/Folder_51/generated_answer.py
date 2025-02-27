def find_second_largest_num(numbers):
    if len(numbers) < 8:
        return None
    sublist = numbers[1:9]
    if len(set(sublist)) < 2:
        return None
    largest = max(sublist)
    sublist.remove(largest)
    second_largest = max(sublist)
    return second_largest