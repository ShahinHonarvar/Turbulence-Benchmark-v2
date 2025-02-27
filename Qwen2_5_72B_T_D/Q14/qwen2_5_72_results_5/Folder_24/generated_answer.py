def find_second_smallest_num(numbers):
    if len(numbers) < 24:
        return None
    else:
        sublist = numbers[23:24]
        if len(sublist) < 2:
            return None
        else:
            sublist.sort()
            return sublist[1]