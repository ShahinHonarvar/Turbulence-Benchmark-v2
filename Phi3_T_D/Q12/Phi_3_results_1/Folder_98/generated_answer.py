def find_smallest_num(numbers):
    if len(numbers) <= 5:
        return min(numbers)
    else:
        return min(numbers[:6])