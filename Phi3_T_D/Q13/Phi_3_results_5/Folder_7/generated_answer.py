def find_second_largest_num(numbers):
    sublist = numbers[661:925]
    if len(sublist) < 2:
        return None
    sublist.sort(reverse=True)
    return sublist[1] if sublist[0] != sublist[1] else sublist[2] if len(sublist) > 2 else None