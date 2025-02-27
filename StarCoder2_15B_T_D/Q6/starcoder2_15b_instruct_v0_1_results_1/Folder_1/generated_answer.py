def all_neg_ints_exclusive(numbers):
    negative_numbers = []
    for i, num in enumerate(numbers):
        if num < 0 and 66 < i < 90:
            negative_numbers.append(num)
    return negative_numbers