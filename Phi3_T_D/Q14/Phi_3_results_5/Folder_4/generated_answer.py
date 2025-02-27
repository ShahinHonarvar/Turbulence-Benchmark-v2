def find_second_smallest_num(lst):
    start, end = (70, min(84, len(lst)))
    if end - start < 4:
        return None
    second_smallest = max(lst[start:end + 1])
    for num in lst[start:end]:
        if num < second_smallest:
            second_smallest = num
    return second_smallest