def find_largest_num(numbers):
    """Find the largest element from index 22 to index 88, both inclusive."""
    largest = numbers[22]
    for num in numbers[22:89]:
        if num > largest:
            largest = num
    return largest