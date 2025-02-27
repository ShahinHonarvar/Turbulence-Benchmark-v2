def find_second_smallest_num(numbers):
    sublist = numbers[70:201]
    if len(sublist) < 2:
        return None
    smallest = min(sublist[0], sublist[1])
    second_smallest = max(sublist[0], sublist[1])
    for num in sublist[2:]:
        if num <= smallest:
            smallest, second_smallest = (num, smallest)
        elif num < second_smallest:
            second_smallest = num
    return second_smallest if second_smallest != smallest else None