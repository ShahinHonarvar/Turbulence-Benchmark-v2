def find_second_smallest_num(numbers):
    if len(numbers) < 3:
        return None
    first_three = numbers[:3]
    first_three.sort()
    return first_three[1]