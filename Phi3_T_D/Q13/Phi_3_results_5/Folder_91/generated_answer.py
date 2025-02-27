def find_second_largest_num(numbers):
    if len(numbers) < 5 or max(numbers[:6]) < max(numbers[:6][:-1]):
        return None
    return max([num for num in numbers if num < max(numbers[:6])])