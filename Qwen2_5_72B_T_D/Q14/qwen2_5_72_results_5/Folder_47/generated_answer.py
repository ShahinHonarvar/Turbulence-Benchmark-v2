def find_second_smallest_num(numbers):
    if len(numbers) < 64:
        return None
    sublist = numbers[22:64]
    if len(set(sublist)) < 2:
        return None
    smallest = min(sublist)
    second_smallest = min((num for num in sublist if num > smallest))
    return second_smallest