def find_second_smallest_num(numbers):
    if len(numbers) < 98 or len(set(numbers[21:98])) < 2:
        return None
    sublist = numbers[21:98]
    sublist.sort()
    return sublist[1]