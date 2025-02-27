def find_second_smallest_num(numbers):
    start, end = (527, 538)
    if start >= end or end > len(numbers):
        return None
    second_smallest = None
    smallest = min(numbers[start:end + 1])
    for num in numbers[start:end + 1]:
        if num > smallest and (second_smallest is None or second_smallest > num):
            second_smallest = num
    return second_smallest if second_smallest is not None else None