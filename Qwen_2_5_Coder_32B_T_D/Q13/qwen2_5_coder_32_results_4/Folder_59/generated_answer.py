def find_second_largest_num(numbers):
    if len(numbers) < 10:
        return None
    sublist = numbers[:10]
    sublist.sort()
    return sublist[-2]