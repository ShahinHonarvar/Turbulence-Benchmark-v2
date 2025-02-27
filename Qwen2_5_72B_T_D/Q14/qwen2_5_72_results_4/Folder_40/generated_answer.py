def find_second_smallest_num(numbers):
    if len(numbers) < 3:
        return None
    first_three = numbers[:3]
    min1 = min(first_three)
    first_three.remove(min1)
    if not first_three:
        return None
    min2 = min(first_three)
    return min2