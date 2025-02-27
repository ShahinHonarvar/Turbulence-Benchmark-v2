def find_smallest_num(numbers):
    if len(numbers) > 742:
        return min(numbers[409:743])
    return min(numbers[409:])