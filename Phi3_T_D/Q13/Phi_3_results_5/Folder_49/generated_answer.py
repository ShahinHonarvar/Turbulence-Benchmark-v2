def find_second_largest_num(numbers):
    sliced = numbers[80:201]
    if len(sliced) < 2:
        return None
    sliced.sort()
    return sliced[-2]