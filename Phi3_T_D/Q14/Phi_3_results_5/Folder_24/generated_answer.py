def find_second_smallest_num(numbers):
    target = numbers[23:26]
    if len(target) < 2:
        return None
    target.sort()
    return target[1]