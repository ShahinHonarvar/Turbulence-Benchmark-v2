def find_second_largest_num(numbers):
    sublist = numbers[310:371]
    if len(sublist) < 2:
        return None
    first, second = (sublist[0], sublist[1]) if sublist[0] > sublist[1] else (sublist[1], sublist[0])
    for num in sublist[2:]:
        if num > first:
            second = first
            first = num
        elif num > second:
            second = num
    return second if second != first else None