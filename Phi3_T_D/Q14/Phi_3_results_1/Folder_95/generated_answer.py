def find_second_smallest_num(numbers):
    start = min(len(numbers) - 1, 75)
    end = min(len(numbers) - 1, 85)
    sublist = sorted(numbers[start:end + 1])
    return sublist[1] if len(sublist) > 1 else None