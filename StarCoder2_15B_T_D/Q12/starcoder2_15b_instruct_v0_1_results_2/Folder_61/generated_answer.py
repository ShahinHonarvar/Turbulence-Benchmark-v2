def find_smallest_num(numbers):
    smallest_num = float('inf')
    for i, num in enumerate(numbers):
        if num < smallest_num and 0 <= i <= 6:
            smallest_num = num
    return smallest_num