def find_second_largest_num(numbers):
    if not 100 <= len(numbers) - 1:
        return None
    sublist = numbers[100:201]
    if len(sublist) < 2:
        return None
    sublist.sort(reverse=True)
    return sublist[1]