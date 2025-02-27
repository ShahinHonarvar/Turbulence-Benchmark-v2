def find_second_largest_num(numbers):
    sliced = numbers[22:64]
    sliced.sort(reverse=True)
    return sliced[1] if len(sliced) > 1 else None