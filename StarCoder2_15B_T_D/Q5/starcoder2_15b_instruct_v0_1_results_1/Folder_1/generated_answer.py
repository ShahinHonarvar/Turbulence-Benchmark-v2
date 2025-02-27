def all_neg_ints_inclusive(numbers):
    output = []
    for i, num in enumerate(numbers):
        if num < 0 and 31 <= i <= 72:
            output.append(num)
    return output